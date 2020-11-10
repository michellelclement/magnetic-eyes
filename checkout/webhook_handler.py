from django.http import HttpResponse


class StripeWH_Handler:
    # To handle stripe webhooks
    def __init__(self, request):
        self.request = request

    # Handle unknown/generic/unexpected webhook event
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Handle payment intent succeeded webhook from stripe
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean Data in Shipping Details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try:
            order - Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.address.country,
                postcode__iexact=shipping_details.address.postal_code,
                town_or_city__iexact=shipping_details.address.city,
                street_address1__iexact=shipping_details.address.line1,
                street_address2__iexact=shipping_details.address.line2,
                county__iexact=shipping_details.address.state,
                grand_total=grand_total,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)


        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Handle payment intent failed webhook from stripe
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

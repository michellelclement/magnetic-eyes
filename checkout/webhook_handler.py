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
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Handle payment intent failed webhook from stripe
    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

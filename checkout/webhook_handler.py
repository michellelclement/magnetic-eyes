from django.http import HttpResponse


class StripeWH_Handler:
    # To handle stripe webhooks
    def __init__(self, request):
        self.request = request

    # Handle unknown/generic/unexpected webhook event
    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

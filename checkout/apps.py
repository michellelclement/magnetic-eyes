from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def read(self):
        import checkout.signals

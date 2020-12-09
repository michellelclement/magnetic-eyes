from django.test import TestCase
from sendemail.forms import ContactForm


class TestContactForm(TestCase):


    def test_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_subject_is_required(self):
        form = ContactForm({'subject': ''})
        self.assertFalse(form.is_valid())

    def test_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())

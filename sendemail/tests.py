from django.test import TestCase
from sendemail.forms import ContactForm


class TestContactForm(TestCase):

    def test_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('from_email', form.errors.keys())
        self.assertEqual(form.errors['from_email'][0],
                         'This field is required.')

    def test_subject_is_required(self):
        form = ContactForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')


class TestViews(TestCase):

    def test_view_contact_form(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sendemail/contact.html')

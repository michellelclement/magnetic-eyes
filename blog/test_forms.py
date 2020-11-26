from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_name_is_required(self):
        form = CommentForm({'name': ''})
        self.assertFalse(form.is_valid())

    def test_contact_form_fields_are_explicit(self):
        form = CommentForm()
        self.assertAlmostEqual(form.Meta.Fields, ['name', 'email', 'body'])

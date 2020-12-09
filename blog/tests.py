from django.test import TestCase
from blog.forms import CommentForm


class TestCommentForm(TestCase):

    def test_name_is_required(self):
        form = CommentForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        form = CommentForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_comment_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())

import datetime

from django.http import HttpResponse
from django.test import TestCase
from django.utils import timezone

from .views import index


class ViewTests(TestCase):

    def test_index(self):
        self.assertEqual(index("").content, b"Hello, world. You're at the polls index.")
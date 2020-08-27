from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):
    def test_CV_url_exist(self):
        url = reverse('cv')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

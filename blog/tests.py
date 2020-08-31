from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):
    def test_index_url_exist(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)

    def test_blog_link_on_blog(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertContains(response, "blog")
        self.assertContains(response, "<a href=\"/blog\">")

    def test_cv_link_on_blog(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertContains(response, "cv")
        self.assertContains(response, "<a href=\"/cv\">")

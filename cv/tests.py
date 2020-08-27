from django.test import TestCase
from django.urls import reverse


class CVViewTests(TestCase):
    def test_CV_url_exist(self):
        url = reverse('cv')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)

    def test_cv_link_on_cv(self):
        url = reverse('cv')
        response = self.client.get(url)
        self.assertContains(response, "CV")
        self.assertContains(response, "<a href=\"/cv\">")

    def test_blog_link_on_cv(self):
        url = reverse('cv')
        response = self.client.get(url)
        self.assertContains(response, "blog")
        self.assertContains(response, "<a href=\"/blog\">")

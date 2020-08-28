from django.test import TestCase
from django.urls import reverse

from cv.models import Education, Grade, WorkExperience


class CVViewTests(TestCase):
    def test_cv_url_exist(self):
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


class EducationModelTests(TestCase):
    def test_education_exists(self):
        e = Education()
        self.assertIsNotNone(e)

    def test_grade_exists(self):
        e = Education()
        g = Grade(education=e)
        self.assertIsNotNone(g)

    def test_work_exp_exists(self):
        w = WorkExperience()
        self.assertIsNotNone(w)

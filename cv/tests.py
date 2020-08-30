from django.test import TestCase
from django.urls import reverse

from cv.models import Education, Grade, Work


class CVNavigationTests(TestCase):
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
        w = Work()
        self.assertIsNotNone(w)


class CVViewTests(TestCase):
    def test_labels_visible(self):
        url = reverse('cv')
        response = self.client.get(url)
        self.assertContains(response, "Basics", msg_prefix="Basics section not visible")
        self.assertContains(response, "Work", msg_prefix="Work section not visible")
        self.assertContains(response, "Education", msg_prefix="Education section not visible")

    def test_basics_visible(self):
        #TODO Selenium
        url = reverse('cv')
        response = self.client.get(url)
        self.assertContains(response, "Name")
        self.assertRegex(response, r'\+?[\d|\ ]{10,}\d', msg="CV does not contain phone number")
        self.assertRegex(response, r'\w+.*\@(\w+.*\.\w+.*)', msg="CV does not contain email address")


class CVBasicFormTest(TestCase):
    def test_form_exists(self):
        url = reverse('basic_new')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)


class CVWorkFormTest(TestCase):
    def test_form_exists(self):
        url = reverse('work_new')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)


class CVEducationFormTest(TestCase):
    def test_form_exists(self):
        url = reverse('education_new')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)

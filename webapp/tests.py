import time

import regex as regex
from selenium import webdriver
from unittest import TestCase

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome Beta/Application/chrome.exe"
chromedriver_binary = "chromedriver.exe"


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver_binary, chrome_options=options)

    def tearDown(self):
        self.browser.quit()

    def test_basics_visible(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.assertIn("cv", self.browser.title)

        data_class_elements = self.browser.find_elements_by_class_name('data')
        phone_regex = regex.compile(r'\+?[\d|\ ]{10,}\d')
        email_regex = regex.compile(r'\w+.*\@(\w+.*\.\w+.*)')
        self.assertTrue(any("Name" in data.text for data in data_class_elements),
                        msg="Can't find name in data class")
        self.assertTrue(any(phone_regex.search(data.text) for data in data_class_elements),
                        msg="Can't find phone number in data class")
        self.assertTrue(any(email_regex.search(data.text) for data in data_class_elements),
                        msg="Can't find email in data class")

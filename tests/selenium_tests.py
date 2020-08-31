import regex as regex
from selenium import webdriver
from unittest import TestCase

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome Beta/Application/chrome.exe"
chromedriver_binary = "../chromedriver.exe"


class BasicTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver_binary, options=options)

    def tearDown(self):
        self.browser.quit()

    def test_navigation(self):
        #navigate to index page
        self.browser.get('http://127.0.0.1:8000')

        #url redirects to blog by default
        self.assertTrue(self.browser.current_url == 'http://127.0.0.1:8000/blog/')

        #user scrolls through blog list
        posts = self.browser.find_elements_by_class_name('post')
        self.assertGreaterEqual(len(posts), 4)


    def test_basics_visible(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.assertIn("cv", self.browser.title)

        data_class_elements = self.browser.find_elements_by_class_name('data')
        phone_regex = regex.compile(r'\+?[\d|\ ]{10,}\d')
        email_regex = regex.compile(r'\w+.*\@(\w+.*\.\w+.*)')
        self.assertTrue(any("Name" in data.text for data in data_class_elements),
                        msg="Can't find name on CV page")
        self.assertTrue(any(phone_regex.search(data.text) for data in data_class_elements),
                        msg="Can't find phone number on CV page")
        self.assertTrue(any(email_regex.search(data.text) for data in data_class_elements),
                        msg="Can't find email on CV page")

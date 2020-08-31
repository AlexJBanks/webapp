import time

import regex as regex
from selenium import webdriver
from unittest import TestCase

from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome Beta/Application/chrome.exe"
chromedriver_binary = "../chromedriver.exe"

local_url = 'http://127.0.0.1:8000/'
live_url = 'https://alexjbanks.eu.pythonanywhere.com/'


def url(sub='', live=True):
    if live:
        return live_url + sub
    else:
        return local_url + sub


class BasicTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver_binary, options=options)

    def tearDown(self):
        self.browser.quit()

    def test_navigation(self):
        # navigate to index page
        self.browser.get(url())

        # url redirects to blog by default
        self.assertTrue(self.browser.current_url == url('blog/'))

        # user scrolls through blog list
        posts = self.browser.find_elements_by_class_name('post')
        self.assertGreaterEqual(len(posts), 4)

        # user looks for 'CV' link and navigates to that page
        try:
            cv_link = self.browser.find_element_by_link_text('CV')
        except NoSuchElementException:
            self.fail()

        cv_link.click()
        time.sleep(1)
        self.assertIn('CV', self.browser.title)

    def test_cv_info_visible(self):
        # navigate to cv page
        self.browser.get(url('cv/'))
        self.assertIn("CV", self.browser.title)

        data_class_elements = self.browser.find_elements_by_class_name('data')
        phone_regex = regex.compile(r'\+?[\d|\ ]{10,}\d')
        email_regex = regex.compile(r'\w+.*\@(\w+.*\.\w+.*)')

        # find basic information on the cv
        self.assertTrue(any("Name" in data.text for data in data_class_elements),
                        msg="Can't find name on CV page")
        self.assertTrue(any(phone_regex.search(data.text) for data in data_class_elements),
                        msg="Can't find phone number on CV page")
        self.assertTrue(any(email_regex.search(data.text) for data in data_class_elements),
                        msg="Can't find email on CV page")

        # find Education information on the cv
        self.assertTrue(any("MSci" in data.text for data in data_class_elements),
                        msg="Can't find Uni degree on CV page")
        self.assertTrue(any("Runshaw" in data.text for data in data_class_elements),
                        msg="Can't find A levels on CV page")

        # find Grade information on the cv
        self.assertTrue(any("Computer Science" in data.text for data in data_class_elements),
                        msg="Can't find A levels on CV page")
        self.assertTrue(any("A*" in data.text for data in data_class_elements),
                        msg="Can't find A levels on CV page")
        self.assertTrue(any("Further Mathematics" in data.text for data in data_class_elements),
                        msg="Can't find A levels on CV page")

        # find Work information on the cv
        self.assertTrue(any("Vodafone" in data.text for data in data_class_elements),
                        msg="Can't find Work Experience on CV page")

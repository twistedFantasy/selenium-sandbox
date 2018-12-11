import os
import unittest

from selenium.webdriver.common.keys import Keys

from python3.common.selenium import Selenium, true


USERS = {
    'successfully': {'email': os.getenv('FB_EMAIL'), 'password': os.getenv('FB_PASSWORD')},
    'failed': {'email': os.getenv('FB_EMAIL'), 'password': 'XXXXXXXXXXX'},
    'not_exist': {'email': 'ed42cfb64291e4@gmail.com', 'password': 'XXXXXXXXXXX'},
}


class FacebookTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Selenium.launch({'headless': true(os.getenv('HEADLESS', True))})

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self, email, password):
        """
        Alternatives:
          self.driver.find_element_by_css('[value="Log In"]').click()
        """
        self.driver.get('https://www.facebook.com/')
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()

    def test_login__successfully(self):
        self.login(**USERS['successfully'])
        textarea = self.driver.find_element_by_css_selector('[placeholder*="What\'s on your mind"]')
        assert textarea.is_displayed() and textarea.is_enabled()

    def test_login__failed_wrong_credentials(self):
        self.login(**USERS['failed'])
        assert 'The password you’ve entered is incorrect.' in self.driver.page_source

    def test_login__failed_user_not_exist(self):
        self.login(**USERS['not_exist'])
        assert 'The email you’ve entered doesn’t match any account.' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()

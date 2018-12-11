import os
import unittest

from selenium.webdriver.common.keys import Keys

from python3.common.selenium import Selenium, true


class PythonOrgTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Selenium.launch({'headless': true(os.getenv('HEADLESS', True))})

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_load(self):
        self.driver.get("https://www.python.org/")
        assert "Python" in self.driver.title

    def test_search(self):
        """
        Alternatives:
          driver.find_element_by_name('q')
          driver.find_element_by_css('[type="search"]')
        """
        self.driver.get("https://www.python.org/")
        element = self.driver.find_element_by_id('id-search-field')
        element.clear()
        element.send_keys("pycon")
        element.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source


if __name__ == '__main__':
    unittest.main()

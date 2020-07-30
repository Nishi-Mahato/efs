import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://nishi.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[2]/form/a[1]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        try:
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div/p[2]/b")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
            print("Test Passed")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
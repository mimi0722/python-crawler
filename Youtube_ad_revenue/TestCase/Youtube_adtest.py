from PageObject.execute import Login
from Common.function import *
from selenium import webdriver
import unittest


class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='D:\chromedriver_win32 (1)\chromedriver.exe')
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
        self.driver.get(config_url())
    def test1(self):
        Login(self.driver).Find_ads()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    suiteTest = unittest.TestCase()
    suiteTest.addTest(logingTest('test1'))
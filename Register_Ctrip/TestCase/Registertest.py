from PageObject.execute import Drag_line
from Common.function import *
from selenium import webdriver
import unittest

class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='D:\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.get(config_url())

    def test1(self):
        search = Drag_line(self.driver)
        search.Unlock()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    suiteTest = unittest.TestCase()
    suiteTest.addTest(logingTest('test1'))
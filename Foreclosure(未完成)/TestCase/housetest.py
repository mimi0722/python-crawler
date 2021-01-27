from PageObject.execute import SearchPage
from Common.csv_data import file_data
from Common.function import *
from selenium import webdriver
import unittest

class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = file_data('D:\python-crawler\Foreclosure\Common\data.csv')
        cls.driver = webdriver.Chrome(executable_path='D:\chromedriver_win32 (1)\chromedriver.exe')
        cls.driver.get(config_url())

    def test1(self):
        search = SearchPage(self.driver)
        print(self.data[0])
        res = search.search_houses(self.data[0], self.data[1], self.data[2])
        #self.assertIn('judicial')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    suiteTest = unittest.TestCase()
    suiteTest.addTest(logingTest('test1'))
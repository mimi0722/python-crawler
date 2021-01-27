from Foreclosure.PageObject.execute import SearchPage
from Foreclosure.Common.csv_data import file_data
from Foreclosure.Common.function import *
from selenium import webdriver
import unittest

class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = file_data('C:\\Users\Annie\PycharmProjects\\test\\venv\Foreclosure\Common\data.csv')
        cls.driver = webdriver.Chrome(executable_path='D:\chromedriver_win32 (1)\chromedriver.exe')
        cls.driver.get("https://aomp.judicial.gov.tw/abbs/wkw/WHD2A00.jsp")#config_url)

    def test1(self):
        search = SearchPage(self.driver)
        print(self.data[0])
        res = search.search_houses(self.data[0][0], self.data[0][1], self.data[0][2])
        #self.assertIn('judicial')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    suiteTest = unittest.TestCase()
    suiteTest.addTest(logingTest('test1'))
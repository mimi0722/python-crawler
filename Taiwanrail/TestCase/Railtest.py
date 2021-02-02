from PageObject.execute import Bookticket
from Common.data import *
from Common.function import *
from selenium import webdriver
import unittest

class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='D:\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.get(url)
        self.driver.maximize_window()

    def test1(self):
        search = Bookticket(self.driver)
        search.Perform(id=ID, start=startstation, end=endstation, date=Date, begintime=starttime, finishtime=endtime)
'''
    @classmethod
    def tearDownClass(self):
        self.driver.quit()'''

if __name__ == "__main__":
    suiteTest = unittest.TestCase()
    suiteTest.addTest(logingTest('test1'))


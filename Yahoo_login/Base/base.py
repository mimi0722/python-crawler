from Common.log import FrameLog
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.log = FrameLog().log()
    def findele(self, A, B):
        try:
            self.log.info("通過" + A + "定位,元素是" + B)
            locator = (A, B)
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except:
            self.log.error('locate fails!')
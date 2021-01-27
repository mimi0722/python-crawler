from Common.log import FrameLog
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.log = FrameLog().log()

    def findele(self,*args):
        try:
            print(args)
            self.log.info("通過"+args[0]+"定位,元素是"+args[1])
            # 設定9秒是因為有時候廣告間會有一段緩衝，約 9秒
            return WebDriverWait(self.driver, 9).until(EC.presence_of_element_located((args)))#self.driver.find_element(*args)
        except:
            self.log.error('locate fails!')

    def Choose(self, time_):  # 用來根據廣告的長短類型來分類廣告
        if time_[0:1] == int:  # 考慮到10min以上的廣告
            time.sleep(31)  # 太長的廣告超過30廟後就跳過
            self.driver.quit()
        elif int(time_[0]) * 60 + int(time_[2:]) > 60:  # 超過60s的廣告則略。這部分自由設定
            time.sleep(31)
            self.driver.quit()
        else:
            secs = int(time_[0]) * 60 + int(time_[2:])  # 若第一則廣告在60s以內則播完
            time.sleep(secs)
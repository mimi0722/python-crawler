from selenium.webdriver.common.by import By
from Base.base import Base

class Login(Base):
    def Play(self):
        self.findele(By.XPATH, '//button[@class="ytp-large-play-button ytp-button"]').click()

    def Ads1(self):
        time1 = self.findele(By.XPATH, '//span[@class="ytp-time-duration"]').text  # 第一則廣告的時間
        self.Choose(time1)

    def Ads2(self):
        try:  # 以防只有一則廣告
            time2 = self.findele(By.XPATH, '//span[@class="ytp-time-duration"]').text
            self.Choose(time2)
            self.driver.quit()
        except:
            pass
            self.driver.quit()

    def Find_ads(self):
        self.Play()
        self.Ads1()
        self.Ads2()

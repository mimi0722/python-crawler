'''可根據設定的位置跟條件找出法拍屋'''
from selenium.webdriver.common.by import By
import time
from Base.base import Base
 # 選取地方法院
class SearchPage(Base):
    def choose_court(self, court):
        self.select_(By.NAME, 'court', name=court)
# 到了下一頁，因為我只對房子有興趣，直接點選
    def ensure1(self):
        self.findele(By.XPATH, "//input[@name='button']")

    def looking_for(self):
        self.findele(By.XPATH, '//input[@class="small"]')

    def choose_city(self, city):# 要點選城市後才能選擇區域
        return self.select_(By.ID, 'hsimun', name=city)

    def choose_district(self,district):
        return self.select_(By.ID, 'ctmd', name=district)

    def ensure2(self):
        return self.findele(By.XPATH, "//input[@type='button']").click()

    def downdetails(self):#抓取負責資料
        return self.details()

    def search_houses(self, court, city, district):
        self.choose_court(court=court)
        time.sleep(2)
        self.ensure1().click()
        self.looking_for()
        self.choose_city(city=city)
        self.choose_district(district=district)
        self.ensure2()
        self.downdetails()
        try:
            for i in range(2,10):
                self.findele(By.XPATH, "//table/tbody/tr[2]/td/nobr[%d]"%i).click()#回圈無法在find_element_by_xpath內使用
                time.sleep(1)
                self.downdetails()
                time.sleep(1)
        except:
            pass

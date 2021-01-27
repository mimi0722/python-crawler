from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Base.base import Base

class Drag_line(Base):
    def Agree(self):
        self.findele(By.XPATH, '//a[@class="reg_btn reg_agree"]').click()
# 到了下一頁，因為我只對房子有興趣，直接點選
    def Start(self):
        return self.findele(By.XPATH, '//div[@class="cpt-drop-btn"]')
                     #"//input[@class='small']").click()
    def Long(self):
        return self.findele(By.XPATH, '//div[@class="cpt-bg-bar"]').size['width']

    def Drag(self, start, long):
        ActionChains(self.driver).drag_and_drop_by_offset(start, long, 0).perform()

    def Unlock(self):
        self.Agree()
        self.Drag(self.Start(), self.Long())

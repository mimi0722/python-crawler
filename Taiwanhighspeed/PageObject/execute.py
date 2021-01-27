from selenium.webdriver.common.by import By
import time
from Base.base import Base
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pyautogui
 # 選取地方法院
class Download(Base):
    #同意cookie
    def ensure(self, court):
        self.findele(By.ID, "btn-confirm")
    '''找出圖片名稱'''
    def pic_name(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        img_name = str(soup.find_all('img')[1])[-17:-7]
        print(img_name)
        return img_name
    '''找出圖片位置'''
    def locate_pic(self):
        self.findele(By.ID, "BookingS1Form_homeCaptcha_passCode")
    #按右鍵
    def click_pic(self, location):
        ActionChains(self.driver).context_click(location).perform()
    #點選下載
    def download(self):
        pyautogui.typewrite('v')
    #修改檔名為img_name
    def img_name(self):
        pyautogui.typewrite('img_name')
    #確認
    def enter(self):# 要點選城市後才能選擇區域
        pyautogui.typewrite(['enter'])
    #開啟檔案
    def open_pic(self, name):
        Image.open('C:/Users/Annie/Downloads/'+name+'.jpg').show()

    def download_pic(self):
        self.ensure()
        self.pic_name()
        self.click_pic(self.locate_pic())
        self.download()
        self.img_name()
        time.sleep(2)
        self.enter()
        time.sleep(2)
        self.open_pic(self.img_name())

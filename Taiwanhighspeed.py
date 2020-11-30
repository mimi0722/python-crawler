#這篇把重點放在驗證碼處理，下載圖檔後再開啟，之後就是圖像處理了，先不深入
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys
from PIL import Image

web = webdriver.Chrome(executable_path = r'D:\chromedriver_win32 (1)\chromedriver.exe')# ,options=options)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://irs.thsrc.com.tw/IMINT/'
web.get(url)
time.sleep(1)
'''同意個人資料使用之通知'''
web.find_element_by_xpath('//input[@id="btn-confirm"]').click()
'''找出圖片名稱'''
soup = BeautifulSoup(web.page_source, 'html.parser')
img_name = str(soup.find_all('img')[1])[-17:-7]
'''找出圖片位置'''
img = web.find_element_by_xpath('//img[@id="BookingS1Form_homeCaptcha_passCode"]')
print(type)
ActionChains(web).context_click(img).perform()
pyautogui.typewrite('v')
time.sleep(2)
pyautogui.typewrite(['enter'])
time.sleep(5)
#開起圖檔
img=Image.open('C:/Users/Annie/Downloads/'+img_name+'.jpg')
img.show()

"""用open cv讀取驗證碼
https://github.com/ywchiu/largitdata/blob/master/code/Course_96.ipynb"""



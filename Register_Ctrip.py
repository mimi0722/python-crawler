"""這篇主要是實作攜程網站註冊時需要拖曳的部分，看書的時候決定動手寫試試看，後來覺得我寫的比較簡潔^^"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
web = webdriver.Chrome(executable_path = r'D:\chromedriver_win32 (1)\chromedriver.exe')# ,options=options)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://passport.ctrip.com/user/reg/home'
web.get(url)
time.sleep(1)

agree = web.find_element_by_xpath('//a[@class="reg_btn reg_agree"]').click()
#找出滑塊開始位置
time.sleep(1)
start = web.find_element_by_xpath('//div[@class="cpt-drop-btn"]')
#求出模塊長度
drag = web.find_element_by_xpath('//div[@class="cpt-bg-bar"]')
x = drag.size['width']
ActionChains(web).drag_and_drop_by_offset(start, x, 0).perform()
#drag_and_drop_by_offset(start, x, 0)其中x跟y是距離，可正可負，單位像素

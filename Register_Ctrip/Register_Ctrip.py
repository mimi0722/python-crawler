"""這篇主要是實作攜程網站註冊時需要拖曳的部分，看書的時候決定動手寫試試看，後來覺得我寫的比較簡潔^^"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

web = webdriver.Chrome(executable_path = r'D:\chromedriver_win32 (1)\chromedriver.exe')# ,options=options)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://passport.ctrip.com/user/reg/home'
web.get(url)

def Load(*args):
    return WebDriverWait(web, 5).until(EC.presence_of_element_located((args)))
'''同意隱私政策'''
Load(By.XPATH, '//a[@class="reg_btn reg_agree"]').click()
'''找出滑塊開始位置'''
start = Load(By.XPATH, '//div[@class="cpt-drop-btn"]')
'''求出模塊長度'''
long = Load(By.XPATH, '//div[@class="cpt-bg-bar"]')
x = long.size['width']
'''執行拖曳'''
ActionChains(web).drag_and_drop_by_offset(start, x, 0).perform()
#drag_and_drop_by_offset(start, x, 0)其中x跟y是距離，可正可負，單位像素

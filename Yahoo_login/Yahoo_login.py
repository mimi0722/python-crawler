'''不知為何無法使用cookies，執行後都沒反應'''
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

web = webdriver.Chrome(executable_path = r'D:\chromedriver_win32 (1)\chromedriver.exe')# ,options=options)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://login.yahoo.com/?.src=twfp&.intl=tw&.lang=zh-Hant-TW&.done=https://tw.yahoo.com&activity=uh-signin&pspid=152963594'
username = 'mimi0733'
password = ''
web.get(url)
time.sleep(1)

def Load(A, B):
    locator = (A, B)#直接把(By.ID, "login-username")放入WebDriverWait內會無法執行
    return WebDriverWait(web, 5).until(EC.presence_of_element_located(locator))
"""輸入帳號"""
Load(By.ID, "login-username").send_keys(username)
'''點選下一步'''
Load(By.ID, "login-signin").click()
'''輸入密碼'''
Load(By.ID, 'login-passwd').send_keys(password)
'''再下一步'''
Load(By.ID, 'login-signin').click()
time.sleep(3)
'''因輸入密碼後會回到首頁，此時點選進入信箱'''
Load(By.ID, 'header-mail-button').click()
'''關閉瀏覽器'''
#web.quit()




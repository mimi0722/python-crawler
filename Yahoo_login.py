'''不知為何無法使用cookies，執行後都沒反應'''
from selenium import webdriver
import time

web = webdriver.Chrome(executable_path = r'D:\chromedriver_win32 (1)\chromedriver.exe')# ,options=options)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://login.yahoo.com/?.src=twfp&.intl=tw&.lang=zh-Hant-TW&.done=https://tw.yahoo.com&activity=uh-signin&pspid=152963594'
username = ''
password = ''
web.get(url)
time.sleep(1)

"""輸入帳號"""
web.find_element_by_xpath("//input[@name='username']").send_keys(username)
'''點選下一步'''
web.find_element_by_xpath("//input[@id='login-signin']").click()
'''輸入密碼'''
time.sleep(1)
web.find_element_by_xpath("//input[@id='login-passwd']").send_keys(password)
'''再下一步'''
web.find_element_by_xpath("//button[@id='login-signin']").click()
time.sleep(1)
'''回到首頁後點選進入信箱'''
web.find_element_by_xpath('//span[@class="D(ib) Fz(14px) Fw(b) Lh(24px) Pstart(38px)"]').click()




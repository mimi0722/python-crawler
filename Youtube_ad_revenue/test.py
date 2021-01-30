from selenium import webdriver
import time

url = 'https://www.youtube.com/watch?v=Bm3vM1g-Y4c'
chromedriver_path = 'D:\chromedriver_win32 (1)\chromedriver.exe'
web = webdriver.Chrome(executable_path=chromedriver_path)
for i in range(3):
    print(i)
    web.get(url)
    time.sleep(3)
    web.find_element_by_xpath('//button[@class="ytp-large-play-button ytp-button"]').click()
    time.sleep(3)

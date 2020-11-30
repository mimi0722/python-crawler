from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from scrapy.spiders import Spider
import time
from selenium.webdriver.support.ui import Select
web = webdriver.Chrome(executable_path = 'D:\chromedriver_win32 (1)\chromedriver.exe')
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://aomp.judicial.gov.tw/abbs/wkw/WHD2A00.jsp'
web.get(url)
time.sleep(1)
select = Select(web.find_element_by_name('court'))
select.select_by_index(6)
web.find_element_by_xpath("//input[@name='button']").click()
time.sleep(2)
web.find_element_by_xpath("//input[@class='small']").click()
time.sleep(4)
select = Select(web.find_element_by_name('hsimun'))#選擇縣市
select.select_by_index(1)
select = Select(web.find_element_by_name('ctmd'))#選擇區域
select.select_by_index(18)
web.find_element_by_xpath("//input[@type='button']").click()
time.sleep(3)
#for i in range(2, 16):   回圈無法在find_element_by_xpath內使用
#   web.find_element_by_xpath('//table[@width="100%"]/tbody/tr[i]/td[6]').text
soup = BeautifulSoup(web.page_source, 'html.parser')
table = soup.find_all('tbody')[2]
caselist = []
f = open("foreclosuredata.txt", 'w')
thelast = table.find_all('tr')[-1].find_all('td')[0].text #找出該頁最後一個按鍵的編號
for i in range(1, int(thelast)+1):
    value = table.find_all('tr')[i].find_all('td')[6].text.replace(',','') #列出底價,並用replace去除逗號
    all = table.find_all('tr')[i].find_all('td')[5].text.strip(' ')#找出產權比例那行
    locations = table.find_all('tr')[i].find_all('td')[4].text.strip(' ')
    if int(value) > 1000000 and '全部' in all and all[16:30] not in caselist: #找出100萬以上及全部產權的物件
        location = locations[:3]+locations[21:24] #因沒辦法完全用strip濾掉空格
        caselist.append(all[16:30]) #這樣設定是確保地址都能列出
        f.write(location)
        f.write(all[16:30])
        f.write(value)
f.close()
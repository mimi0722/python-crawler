'''可根據設定的不同位置跟條件找出法拍屋'''
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#注意臺字寫法會影響結果
items = (['臺中市','北區'])#,['高雄市','鳳山區','三民區'])

url = 'https://aomp109.judicial.gov.tw/judbp/wkw/WHD1A02.htm'
web = webdriver.Chrome(executable_path = 'D:\chromedriver_win32 (1)\chromedriver.exe')
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
web.get(url)

#建立select選單
def select(element, text):
    select = Select(web.find_element_by_id(element))
    select.select_by_visible_text(text)

def button(cli):
    web.find_element_by_xpath(cli).click()
'''產權是全部並一百萬以上的法拍屋，然後存在名為'Foreclosure'的檔案內'''
def Wait(*args):
    return WebDriverWait(web, 10).until(EC.presence_of_element_located((args)))
def details():
    soup = BeautifulSoup(web.page_source, 'html.parser')
    table = soup.find_all('tbody')[2]
    for i in range(1, 16):
        try:
            value = table.find_all('tr')[i].find_all('td')[6].text.replace(',','') #列出底價,並用replace去除逗號
            all = table.find_all('tr')[i].find_all('td')[5].text#找出產權比例那行
            if int(value) > 1000000 and '全部' in all: #找出100萬以上及全部產權的物件
                print(all.strip(' '))
                f = open('foreclosure', 'a', encoding="utf-8")
                f.write(table.find_all('tr')[i].find_all('td')[5].text[67:76])#坪數
                f.write(table.find_all('tr')[i].find_all('td')[5].text[16:40])#地址
        except:
            f.close()

'''點選城市'''
#for i in items:
#WebDriverWait(web, 20).until(EC.presence_of_element_located((By.ID, 'county')))
time.sleep(5)
#select('county', '臺中市')
'''區域預設為全部，取消全部'''
#web.find_element_by_id('townChkBtn').click()
'''選擇區域'''
#web.find_element_by_xpath('//div[@value="北區"]').click()
'''選擇全部產權'''
web.find_element_by_css_selector("rrange_ALL").click()
#for i in range(2, 16):   回圈無法在find_element_by_xpath內使用
#   web.find_element_by_xpath('//table[@width="100%"]/tbody/tr[i]/td[6]').text
'''因為無法找到最後一頁是多少，先設定20這個數字。持續點選下一頁並抓取資料'''
#try:
#    for item in range(2, 20):
#        button("//nobr[%i]"% (item))
#        details()
#except:
#    pass

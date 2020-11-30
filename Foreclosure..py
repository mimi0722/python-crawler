'''可根據設定的位置跟條件找出法拍屋'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select

court_name = '臺灣臺中地方法院'#注意臺字寫法會影響結果
city = '臺中市'
district = '北區'

web = webdriver.Chrome(executable_path = 'D:\chromedriver_win32 (1)\chromedriver.exe')
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
url = 'https://aomp.judicial.gov.tw/abbs/wkw/WHD2A00.jsp'
web.get(url)

#建立select選單
def select(element, text):
    select = Select(web.find_element_by_name(element))
    select.select_by_visible_text(text)

def button(cli):
    web.find_element_by_xpath(cli).click()

#選取地方法院
select('court', court_name)
button("//input[@name='button']")
time.sleep(1)
#到了下一頁，因為我只對房子有興趣，直接點選
button("//input[@class='small']")
time.sleep(1)
#要點選城市後才能選擇區域
select('hsimun', city)
select('ctmd', district)
button("//input[@type='button']")
time.sleep(1)
#for i in range(2, 16):   回圈無法在find_element_by_xpath內使用
#   web.find_element_by_xpath('//table[@width="100%"]/tbody/tr[i]/td[6]').text
soup = BeautifulSoup(web.page_source, 'html.parser')
table = soup.find_all('tbody')[2]
#在下方有顯示資料數，找出後放入迴圈才不會error，考慮到可能是二位數所以再處理
if str.isdigit(soup.find_all('tbody')[3].find('tr').find('td').text[8]) is True:
    number = soup.find_all('tbody')[3].find('tr').find('td').text[7:9]
else:
    number = soup.find_all('tbody')[3].find('tr').find('td').text[7]

for i in range(1, int(number)+1):
    value = table.find_all('tr')[i].find_all('td')[6].text.replace(',','') #列出底價,並用replace去除逗號
    all = table.find_all('tr')[i].find_all('td')[5].text#找出產權比例那行
    if int(value) > 1000000 and '全部' in all: #找出100萬以上及全部產權的物件
        print(all.strip(' '))
        f = open('foreclosure', 'a', encoding="utf-8")
        f.write(table.find_all('tr')[i].find_all('td')[5].text[67:76])#坪數
        f.write(table.find_all('tr')[i].find_all('td')[5].text[16:40])#地址
        f.close()
        break


from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from Foreclosure.Common.log import FrameLog

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.log = FrameLog().log()

    def findele(self,*args):
        try:
            print(args)
            self.log.info("通過"+args[0]+"定位,元素是"+args[1])
            return self.driver.find_element(*args)
        except:
            self.log.error('locate fails!')

    def select_(self, *args, name):
        self.select = Select(self.findele(*args))
        self.select.select_by_visible_text(name)

    #def click(self, args):
    #    self.findele(args).click()

    def details(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        table = soup.find_all('tbody')[2]
    # 在下方有顯示資料數，找出後放入迴圈才不會error，考慮到可能是二位數所以再處理\
        try:
            for i in range(1, 16):
                value = table.find_all('tr')[i].find_all('td')[6].text.replace(',', '')# 列出底價,並用replace去除逗號
                all = table.find_all('tr')[i].find_all('td')[5].text  # 找出產權比例那行
                if int(value) < 1000000 and '全部' in all:  # 找出100萬以上及全部產權的物件
                    print(all.strip(' '))
                    f = open('result.txt', 'a', encoding="utf-8")
                    f.write(table.find_all('tr')[i].find_all('td')[5].text[67:76])  # 坪數
                    f.write(table.find_all('t')[i].find_all('td')[5].text[16:40])  # 地址
            f.close()
        except:
            pass

    def url(self):
        return self.driver.current_url
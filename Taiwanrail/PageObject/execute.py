'''可根據設定的位置跟條件找出法拍屋'''
from selenium.webdriver.common.by import By
import time
from Base.base import Base, types
from Common.data import Traintype
 # 選取地方法院
class Bookticket(Base):
    #輸入身分證
    def TypeID(self, id):
        self.findele(By.ID, 'pid').send_keys(id)
    #輸入出發地點
    def Departure(self, A):
        self.findele(By.ID, "startStation").send_keys(A)
    #輸入到達地點
    def Arrive(self, B):
        self.findele(By.ID, 'endStation').send_keys(B)
    #選擇依時間選車
    def Decidedbytime(self):
        self.findele(By.XPATH, "//label[@for='orderType2']").click()
    #輸入日期
    def Choosedate(self, Date):
        self.findele(By.ID, "rideDate1").clear()
        js = "document.getElementById('rideDate1').value = '%s'" % (Date)
        self.driver.execute_script(js)
    # 選取出發時間範圍
    def Timeranges(self,starttime, endtime):
        self.select_(By.ID, "startTime1", name=starttime)
        self.select_(By.ID, "endTime1", name=endtime)
    #選擇車種
    def Choosetype(self):
        self.findele(By.XPATH, '//label[@for="%s"]' % (str(types[Traintype]))).click()

    def Perform(self, id, start, end, date, begintime, finishtime):
        self.TypeID(id)
        self.Departure(start)
        self.Arrive(end)
        self.Decidedbytime()
        self.Choosedate(Date=date)
        self.Timeranges(starttime=begintime, endtime=finishtime)
        self.Choosetype()
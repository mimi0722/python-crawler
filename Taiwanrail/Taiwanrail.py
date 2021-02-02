from selenium import webdriver
from selenium.webdriver.support.ui import Select

if __name__ == '__main__':
    url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query'
    chromedriver_path = 'D:\chromedriver_win32 (1)\chromedriver.exe'
    web = webdriver.Chrome(executable_path=chromedriver_path)
    web.get(url)
    web.maximize_window()
    #以下選項可更改，包刮Traintype
    ID = 'S278882512'
    startstation = '高雄'
    endstation = '臺中'
    starttime = '17:00'
    endtime = '19:00'
    Date = ('2021/02/02')
    Traintype = '自強'
    #輸入身分證
    web.find_element_by_id('pid').send_keys(ID)
    #輸入起站
    web.find_element_by_id("startStation").send_keys(startstation)
    #輸入迄站
    web.find_element_by_id("endStation").send_keys(endstation)
    #選擇依時段訂車
    web.find_element_by_xpath("//label[@for='orderType2']").click()
    #選擇日期
    web.find_element_by_id("rideDate1").clear()
    js = "document.getElementById('rideDate1').value = '%s'"  %  (Date)
    web.execute_script(js)
    #選取出發時間範圍
    select = Select(web.find_element_by_id("startTime1"))
    select.select_by_visible_text(starttime)
    select = Select(web.find_element_by_id("endTime1"))
    select.select_by_visible_text(endtime)
    #選擇車種
    types = {'太魯閣':'ticketOrderParamList0.trainTypeList1',
            '普悠瑪':'ticketOrderParamList0.trainTypeList2',
            '自強':'ticketOrderParamList0.trainTypeList3',
            '莒光':'ticketOrderParamList0.trainTypeList4',
            '復興':'ticketOrderParamList0.trainTypeList5'}

    web.find_element_by_xpath('//label[@for="%s"]' % (str(types[Traintype])) ).click()



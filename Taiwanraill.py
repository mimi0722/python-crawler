#台鐵訂票機器人，但無法破解機器人認證
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

start_station = '鳳山'
end_station = '彰化'
date = '2020/12/05'
#選擇最早出發時間
time_range_from = '13:00'
#選擇最晚出發時間
time_range_to = '15:00'
train_type = '莒光'

url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query'
web = webdriver.Chrome(executable_path = 'D:\chromedriver_win32 (1)\chromedriver.exe')
web.maximize_window()
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
web.get(url)
time.sleep(3)
#輸入身分證字號
web.find_element_by_xpath('//input[@class="idmember pid form-input"]').send_keys('S278882512')
web.find_element_by_xpath('//input[@id="startStation"]').send_keys(start_station)
web.find_element_by_xpath('//input[@id="endStation"]').send_keys(end_station)
#用點選的一直在縣市沒問題，可是到站名的選擇時，大站像高雄、新左營就沒辦法成功
#web.find_element_by_xpath("//*[contains(text(),'高雄市')]").click()
#web.find_element_by_xpath("//[text()='路竹']").click()
#有試著將上面方法改為函數，但一直沒成功
#def choose_station(name):
#    web.find_element_by_xpath("//*[contains(text(), name)]").click()
#點選依時段買票，但有些方法無法成功
#period = web.find_element_by_xpath('//input[@id="orderType2"]').clicck()
#web.find_element_by_xpath("//[contains(text(),'依時段')]").click()
time.sleep(1)
period = web.find_element_by_xpath('//input[@id="orderType2"]')#.click()
ActionChains(web).click(period).perform()
#輸入日期
web.find_element_by_xpath('//input[@id="rideDate1"]').clear()
#輸入日期。因為是readonly所以不能用send_keys輸入日期，會變成像是2020//1/2
#js = "$('input[id=rideDate1]').removeAttr('readonly')"
js = 'document.getElementById("rideDate1").value="2020/12/02"'
web.execute_script(js)
#web.find_element_by_id('rideDate1').send_keys('2020/12/2')
#選擇最早出發時間
select = Select(web.find_element_by_id("startTime1"))
select.select_by_visible_text(time_range_from)
#選擇最晚出發時間
select = Select(web.find_element_by_id("endTime1"))
select.select_by_visible_text(time_range_to)
#選擇車種
#web.find_element_by_xpath("//*[text()='自強']").click()定位不到
trains = {'普悠瑪':"ticketOrderParamList0.trainTypeList1",
          '太魯閣':'ticketOrderParamList0.trainTypeList2',
          '自強':"ticketOrderParamList0.trainTypeList3",
          '莒光':"ticketOrderParamList0.trainTypeList4",
          '區間':'ticketOrderParamList0.trainTypeList5'}
type = web.find_element_by_id(trains[train_type])#
ActionChains(web).click(type).perform()#.click()

















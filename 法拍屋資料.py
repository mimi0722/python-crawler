from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

#This code is about finding out specific forceclosed house data.

#目前看來對於不同的選擇，像選單或者是用滑鼠點選的選項都有不同的方法，
#即使像選單，對於不同的方法也會有不同的find_element_by
#若同一頁面要操作不同選單，就不能用以下"高雄地方法院"那個方法，一旦用了之後其他
#同一頁面選單會沒辦法定位

if __name__ == '__main__':
    url = 'http://aomp.judicial.gov.tw/abbs/wkw/WHD2A00.jsp'
    chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
    
    driver = webdriver.Chrome(executable_path = chromedriver_path)
    driver.set_page_load_timeout(60)
    driver.get(url)
        
    for option in driver.find_elements_by_tag_name('option'):#注意這種選單
        if option.text == '臺灣高雄地方法院':                #要用tag_name
            option.click()

    #option = driver.find_elements_by_tag_name('option')#
    #option[13].click() #這種比上面的好用，而且不像上面那個一頁只能用一次

    element = driver.find_element_by_name('button').click()
    
    path1 = "/html/body/form/table/tbody/tr/td/div/div/center/table/tbody/tr/td/div/font/input"
    element = driver.find_element_by_xpath(path1).click()

    select = Select(driver.find_element_by_id('hsimun'))#此時這個方法可以用by_id
    select.select_by_visible_text('高雄市')

    #for option in driver.find_elements_by_tag_name('option'):
    #    if option.text =='三民區':
    #        option.click() #如果用這一段，那就無法用在別的選單，即使用了
    #下面兩行三民區的方法也一樣。連點交那欄的選單也無法操作。總之這個方法能不用
    #就不用
    username = driver.find_elements_by_name('checkyn')
    username[1].click()#另一種選取選項的方法，此為選取是否為點交
    
    select = Select(driver.find_element_by_id('ctmd'))#這個方法不受
    select.select_by_visible_text('三民區')        #同一頁面多選單影響
    
    #check_path = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td/input#checkyn"
    #for element in driver.find_elements_by_xpath(check_path):
    #    if element.text== '是':
    #        element.click() #這個程式碼不管怎樣都無法運作

    #dtrc_path = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td/select#ctmd/option"
    #for option in driver.find_elements_by_xpath(dtrc_path):
    #    if option.text== '鳳山區':
    #        option.click()      #這個也是           
    
            
    path2 = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/input"
    element = driver.find_element_by_xpath(path2).click()

    time.sleep(5)

    try:
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        table = soup.find('table')
        results = table.find_all('tr')
        for i in range(6, 21):
            if int(results[i].find_all('td')[6].text.strip().replace(',','')) <=2000000:
                print(results[i].find_all('td')[6].text.strip().replace(',',''))
            else:
                print('nothing match')
    except:
        print('loading fail')
    
    

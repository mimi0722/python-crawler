
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import re

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=HCeLWGU4hZM&list=PLXWBxxhUoqDd0rJueoo4Q9841KgubhUXj&index=1'
    #一系列清單的url會隨更新而變化，故若不是從第一個開始撥放就有可能有更新
    chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    # river.set_page_load_timeout(15)#這個用的話載入會變慢
    time.sleep(3)  # sleep()的設定秒數根次數會影響到載入的流暢度跟程式執行的成功率
    driver.get(url)
    #element = driver.find_element_by_tag_name('button').click()#因有時開啟瀏覽器會無法撥放，但後來發現定位不到撥放鍵
    time.sleep(10)


    def start():
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        times_ = soup.find_all('div', 'ytp-ad-text')
        try:
            if times_[0].text.strip() == '第 1 則廣告 (共 2 則) · 1':
                secs = times_[1].text.strip()[0] * 60 + times_[1].text.strip()[2:]
                time.sleep(secs)
            for time_ in times_:
                print(time_.text, 1)
                ret_match = re.findall(r"\d\S\d\d", time_.text)
                if len(ret_match) != 0:
                    print(ret_match, 2)
                    selected = ret_match[0]
                    break
            if int(selected[-2:]) >= 30:
                time.sleep(35)  # 根據查到的資料，30秒即為有效觀看
                print('a')
            else:
                time.sleep(int(selected[-2:]))
                print('b')
        except:
            print('c')
            # time.sleep(30)
            pass


    start()
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    name = soup.find_all('span', {'class': 'style-scope ytd-playlist-panel-video-renderer'})
    for i in range(6,len(name) + 1,4):#每一部影片中有同樣'span'跟'class'就有3個，讓range從3開始就是從第二部影片開始
        try:
            print(name[i].text,i)
            driver.find_element_by_partial_link_text(name[i].text.strip()).click()
            time.sleep(30)#要讓影片播一段時間才能有比較多的廣告出現
            start()#可能是硬體設備的關係，有時候廣告播完後才爬，但已經爬不到
        except:
            pass



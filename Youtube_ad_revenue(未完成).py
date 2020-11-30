#這隻爬蟲是用來在Youtube影片一開始顯示廣告的時候，若有兩個廣告，在第一支廣告在廣告超過60s後跳過廣告並到下一支影片(可以過濾掉太長的影片)。若第一支廣告不超過60s，
#則等等到第二支廣告超過30s後跳到下一個廣告之所以設定30s是因為根據查到的資料，影片只要撥放超過30sYoutuber就能獲利
#原本是希望找出每個影片中所有的廣告，但因Youtuber放置廣告的時間都不一樣，也無法從爬蟲找到廣告位置，因此決定把主力放在影片的開頭廣告上
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import re
import lxml

if __name__ == '__main__':
    url = 'https://www.youtube.com/playlist?list=PLhZ2FyUKfBD8oBGfiofkbrVEJ_s59sEFW'
               #一系列清單的url會隨更新而變化，故若不是從第一個開始撥放就有可能有更新
    chromedriver_path = 'D:\chromedriver_win32 (1)\chromedriver.exe'
    web = webdriver.Chrome(executable_path=chromedriver_path)
    time.sleep(3)# river.set_page_load_timeout(15)#這個用的話載入會變慢
    web.get(url)
    web.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-thumbnail-overlay-side-panel-renderer']").click()

    def start():
        soup = BeautifulSoup(web.page_source, 'html.parser')
        times_ = soup.find_all('div', 'ytp-ad-text')
        try:
            time.sleep(5)
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
                web.find_element_by_id("//div[@class = 'ytp-ad-text ytp-ad-skip-button-text']").click()
                #超過30s後點選略過廣告
                print('a')
            else:
                time.sleep(int(selected[-2:]))
                print('b')
        except:
            print('c')
            # time.sleep(30)
            pass


    start()
    soup = BeautifulSoup(web.page_source, 'html.parser')
    name = soup.find_all('span', {'class': 'style-scope ytd-playlist-panel-video-renderer'})
    for i in range(6,len(name) + 1,4):#每一部影片中有同樣'span'跟'class'就有3個，讓range從3開始就是從第二部影片開始
        try:
            print(name[i].text,i)
            web.find_element_by_partial_link_text(name[i].text.strip()).click()
            time.sleep(30)#要讓影片播一段時間才能有比較多的廣告出現
            start()#可能是硬體設備的關係，有時候廣告播完後才爬，但已經爬不到
        except:
            pass



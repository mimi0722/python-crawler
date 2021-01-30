#這隻爬蟲是用來在Youtube影片一開始顯示廣告的時候，若有兩個廣告，在第一支廣告在廣告超過60s後跳過廣告並到下一支影片。若第一支廣告不超過60s，
#根據查到的資料，影片只要撥放超過30sYoutuber就能獲利，所以第二支廣告超過31s後關閉瀏覽器
#原本是希望找出每個影片中所有的廣告，但查過一些資烙後發現即使手動安插廣告也不一定會有廣告出現，另外清單內的影片開頭出現廣告的機率會大減
#結論是選擇一部影片並在開頭兩個廣告播完後關閉然後重開是最有效率的，每次一定有兩個廣告，變成說每次都要開關瀏覽器就是了
#其中N為決定瀏覽器開關的次數
#ps.有測試日誌的版本沒有辦法設定瀏覽器開關次數
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=Bm3vM1g-Y4c'
    N = 3#設定瀏覽器執行次數
    def Wait(*args):
        return WebDriverWait(web, 10).until(EC.presence_of_element_located((args)))
        # 設定9秒是因為有時候廣告間會有一段緩衝，約 9秒
    def Choose(time_):  # 用來根據廣告的長短類型來分類廣告
        if time_[0:1] == int:  # 考慮到10min以上的廣告
            time.sleep(31)  # 太長的廣告超過30廟後就跳過
            web.quit()
        elif int(time_[0]) * 60 + int(time_[2:]) > 60:  # 超過60s的廣告則略。這部分自由設定
            time.sleep(31)
            web.quit()
        else:
            secs = int(time_[0]) * 60 + int(time_[2:])  # 若第一則廣告在60s以內則播完
            time.sleep(secs)
    def Times():
        time1 = Wait(By.XPATH, '//span[@class="ytp-time-duration"]').text  # 第一則廣告的時間
        Choose(time1)  # 對於第一則廣告的篩選
        try:  # 以防只有一則廣告
            time2 = Wait(By.XPATH, '//span[@class="ytp-time-duration"]').text
            Choose(time2)
            web.quit()
        except:
            pass
            web.quit()

    for i in range(N):
        chromedriver_path = 'D:\chromedriver_win32 (1)\chromedriver.exe'
        web = webdriver.Chrome(executable_path=chromedriver_path)
        web.get(url)
        print(i)
        Wait(By.XPATH, '//button[@class="ytp-large-play-button ytp-button"]').click()  # 撥放影片
        Times()

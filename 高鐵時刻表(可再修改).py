"""這篇主要先設定起始站和終點站以及出發的日期時間, 再找出設定時間之後的所有車次
跟出發-抵達時間"""

from bs4 import BeautifulSoup
import requests
import re
url = 'http://m.thsrc.com.tw/tw/TimeTable/SearchResult'

def find_station_id(url):
    dom = requests.get(url, headers=headers)
    soup = BeautifulSoup(dom.text, 'html5lib')
    selects = soup.find('select', {'id':'startStation'})
    _id = selects.find_all('option')
    dic = {}
    for i in _id:
        dic[i.text.strip()] = i['value']
    return dic
    

def output(start_station, end_station, date, time):
    url = 'https://m.thsrc.com.tw/tw/TimeTable/SearchResultList'
    form_data = {
    'startStation': start_station,
    'endStation': end_station,
    'theDay': date,
    'timeSelect': time,
    'waySelect': 'DepartureInMandarin',
    #'RestTime': later_page,
    'EarlyOrLater': '2',
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
    resp = requests.post(url, data = form_data, headers = headers)
    soup = BeautifulSoup(resp.text, 'html5lib')
    later_page = soup.find_all('a', {'id':'laterTimeLink'})[0]['onclick']
    #later_page是下一頁的關鍵
    result = []
    time = later_page[17:22]
    divs0 = soup.find_all('div', "ui-block-a")
    divs1 = soup.find_all('div', "ui-block-b")
    for i in range(len(divs0)):
        if divs1[i].text.strip()=='商務車廂':
            break
        print(divs0[i].text.strip(), divs1[i].text.strip().strip(' '), i)
    #result.append([divs0[i].text.strip(), divs1[i].text.strip()]) 以list儲存會有別的數字參雜, 先放著之後處理
    #print("".join(divs1[2].text.strip())) 這個方法想去掉中間的空格但失敗了
    

    if later_page =="RestTrainSubmit('', '2');":
        return None
    else:
        return output(start_station, end_station, date, time)


if __name__ == '__main__':      
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
    dic = find_station_id(url)
    print(output(dic['台北站'], dic['左營站'], '2019/10/30', '15:00'))

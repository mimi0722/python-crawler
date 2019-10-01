from bs4 import BeautifulSoup
import requests
url = 'http://m.thsrc.com.tw/tw/TimeTable/SearchResult'

def find_station_id(url):
    dom = requests.get(url, headers=headers)
    soup = BeautifulSoup(dom.text, 'html5lib')
    selects = soup.find('select', {'id':'startStation'})
    _id = selects.find_all('option')
    dic = {}
    for i in _id:
        dic[i.text.strip()] = i['value']
    #print(dic)

    return dic
    

def output(start_station, end_station, date, time):
    form_data = {
        'startStation': start_station,
        'endStation': end_station,
        'theDay': date,
        'timeSelect': time,
        #'waySelect': DepartureInMandarin
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'
               }
    resp = requests.post(url, data = form_data, allow_redirects=False, headers = headers)#, headers=headers)
    print(resp.headers)
    resp2 = requests.get()
    soup = BeautifulSoup(resp.text, 'html5lib')
    print(soup)
    print(3)
    divs = soup.find_all('div', "ui-block-c timeResultListTitle")
    for div in divs:
        print(div)




if __name__ == '__main__':      
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
    dic = find_station_id(url)
    #print(dic)
    #print(dic['台北站'])
    output(dic['台北站'], dic['左營站'], '2019/09/23', '20:00')
    
    
    #date = input('請輸入日期')
    #print(find_station_id(soup))

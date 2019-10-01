headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
import requests
from bs4 import BeautifulSoup
for i in range(1000, 10000):
    print(i)
    url = 'https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID='+str(i)
    re = requests.get(url, headers = headers)
    re.encoding = 'utf8'
    soup = BeautifulSoup(re.text, 'html5lib')
    tables = soup.find_all('table', "solid_1_padding_4_2_tbl")
    try:
        result = tables[-1].find_all('tr')[2].find_all('td')[5]
        if float(result.text[1:])>float(10):
            print(result.text)
    except:
        pass

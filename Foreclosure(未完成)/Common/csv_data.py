import csv
def file_data(file_location):
    with open(file_location, encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        for r in rows:
            return r

if __name__ == '__main__':
    print(file_data('D:\python-crawler\Foreclosure\Common\data.csv'))

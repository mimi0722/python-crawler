import csv
def file_data(file_location):
    with open(file_location, encoding='utf-8') as csvfile:
        dic = {}
        rows = csv.reader(csvfile)
        i = 0
        for r in rows:
            dic[i] = r
            i+=1
    return dic

if __name__ == '__main__':
    print(file_data('C:\\Users\Annie\PycharmProjects\\test\\venv\Foreclosure\Common\data.csv'))

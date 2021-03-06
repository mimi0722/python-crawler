import csv
import os, configparser

def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]

def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "\Common\config.ini")
    return config.get('testUrl', 'url')

def login_data():
    config = configparser.ConfigParser()
    config.read(project_path() + "\Common\config.ini")
    return config.get('login', 'ID'), config.get('login', 'password')
if __name__ == '__main__':
    print(project_path())
    print(config_url())
    print(login_data())
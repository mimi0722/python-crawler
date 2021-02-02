import os, configparser

def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]
if __name__ == '__main__':
    print(project_path())


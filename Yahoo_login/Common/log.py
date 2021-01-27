import logging, time
from Common.function import project_path
class FrameLog():
    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = project_path() + "Logs\\"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'w', encoding='utf-8')
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(asctime)s]   %(filename)s->%(funcName)s line:%(lineno)d\
                                       [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        fh.close()

    def log(self):
        return self.logger

if __name__ == '__main__':
    log = FrameLog().log()
    log.error("error")
    log.debug("debug")
    log.info("info")
    log.critical('嚴重')

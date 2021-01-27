from Common.log import FrameLog

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.log = FrameLog().log()

    def findele(self,*args):
        try:
            print(args)
            self.log.info("通過"+args[0]+"定位,元素是"+args[1])
            return self.driver.find_element(*args)
        except:
            self.log.error('locate fails!')
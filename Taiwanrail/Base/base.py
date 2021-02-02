from selenium.webdriver.support.ui import Select
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

    def select_(self, *args, name):
        self.select = Select(self.findele(*args))
        self.select.select_by_visible_text(name)

types = {'太魯閣':'ticketOrderParamList0.trainTypeList1',
            '普悠瑪':'ticketOrderParamList0.trainTypeList2',
            '自強':'ticketOrderParamList0.trainTypeList3',
            '莒光':'ticketOrderParamList0.trainTypeList4',
            '復興':'ticketOrderParamList0.trainTypeList5'}
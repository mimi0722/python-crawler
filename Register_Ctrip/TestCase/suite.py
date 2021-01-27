import unittest
import HTMLTestRunner
import time
from Foreclosure.Common.function import project_path

if __name__ == '__main__':
    test_dir= project_path() + "Common\TestCases"
    tests = unittest.defaultTestLoader.discover(test_dir,
                                                pattern = 'house*.py',)
                                                #top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = project_path() + "\Reports\\"+now +'.html'
    print(filepath)
    fp=open(filepath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自動化測試報告', description=u'測試報告')
    runner.run(tests)
    fp.close()
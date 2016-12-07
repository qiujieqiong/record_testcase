"""Running tests"""

import time
from unittest import TextTestRunner,TextTestResult
from lib import utils

class QTestResult(TextTestResult):

    def addError(self, test, err):
        super(QTestResult, self).addError(test, err)
        self.log(False,test)

    def addFailure(self, test, err):
        super(QTestResult, self).addFailure(test, err)
        self.log(False,test)
    def addSuccess(self, test):
        super(QTestResult, self).addSuccess(test)   
        self.log(True,test)
    
    def startTest(self, test):
        super(QTestResult, self).startTest(test)
        self.startTime=time.time()

    def log(self,re,test):
        seconds = "%.3f" % (time.time() - self.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        utils.commitresult(type(test).caseid, re, minutes)

qRunner=TextTestRunner(resultclass=QTestResult)
def runTest(testcase):
    qRunner.run(testcase)
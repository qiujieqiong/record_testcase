"""Running tests"""

import time
from unittest import TextTestRunner,TextTestResult
from lib import utils

class QTestResult(TextTestResult):

    def startTest(self, test):
        super(QTestResult, self).startTest(test)
        self.test = test

    def stopTestRun(self):
        re=len(self.failures) == 0 and len(self.errors) == 0 
        caseid = type(self.test).caseid     
        seconds = "%.3f" % (time.time() - self.startTime)
        minutes = convertToMinutes(float(seconds))
        commitresult(caseid, re, minutes)
        
    def startTestRun(self):
        self.startTime=time.time()

qRunner=TextTestRunner(resultclass=QTestResult)
def runTest(testcase):
    qRunner.run(testcase)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.executeTestCase import runTest
import importlib
import os 
import re
from lib import utils

def getIdFile():
    return ["2","3"]



def getClass(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            match = re.match('class (.*)\(unittest.TestCase',line)
            if match:
                return match.group(1)
    raise Exception(file +' has no class ')


    
def main():
    idlist = getIdFile()
    classes = []
    casedirs = ["dde_launcher"]
    for casedir in casedirs:
       files = os.listdir(casedir)
       files=list(filter(lambda e : e.startswith("test"),files))
       for f in files:
            module = importlib.import_module(".".join((casedir, f[:-3])))
            class_name = getClass(os.sep.join((casedir, f)))
            testClass = getattr(module,class_name)
            if hasattr(module,"caseid"):
                testClass.caseid=getattr(module,"caseid")
            classes.append(testClass)

    classes=list(filter(lambda e:e.caseid in idlist,classes))
    for c in classes:
        runTest(c.suite())
if __name__ == '__main__':
    main()

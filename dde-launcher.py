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
    listdir = ["dde_launcher"]
    for adir in listdir:
       files = os.listdir(adir)
       files=list(filter(lambda e : e.startswith("test"),files))
       for f in files:
            m=importlib.import_module(adir+"."+f[:-3])
            na = getClass(adir+"/"+f)
            testClass =getattr(m,na)
            if hasattr(m,"caseid"):
                testClass.caseid=getattr(m,"caseid")
            classes.append(testClass)

    #classes=list(filter(lambda e:e.caseid in idlist,classes))
    for c in classes:
        runTest(c.suite())
if __name__ == '__main__':
    main()

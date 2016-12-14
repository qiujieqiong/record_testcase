#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.executeTestCase import runTest
import importlib
import os
from unittest import TestCase

casedirs=["dde_launcher","dde_dock"]

def getIdFile():
    return ["2","3"]

def getClass(f):
    clas = [ getattr(f,c) for c in dir(f) ]
    clas = [ cla for cla in clas if hasattr(cla,"__bases__") and TestCase in cla.__bases__ ]
    noIdClas=[  cla for cla in clas if not hasattr(cla,"caseid")]
    for ncla in noIdClas:
        ncla.caseid = f.caseid
    return clas

def getAllClass():
    allmodules = [  d+"."+f[:-3] for d in casedirs for f in os.listdir(d) if  f.startswith("test")]
    classes = [getClass(importlib.import_module(f)) for f in allmodules ]
    return [ c  for x in classes for c in x  if  c.caseid in getIdFile() ]

if __name__ == '__main__':
    for c in getAllClass():
        runTest(c)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from time import sleep
from lib import runner,utils
#from lib.launcher import *
#from lib.dde_dock import *


caseid = '33842'
casename = 'all-518:添加到任务栏'

class LauncherAddToDock2(unittest.TestCase):

    caseid='33842'
    @classmethod
    def setUpClass(cls):
        
        '''
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'
        cls.dockname = 'google-chrome'
        dockApps = Dock().getAllDockApps()
        if cls.dockname in dockApps:
            appCoor = Dock().getAppCoor(cls.googleName)
            screen = pyautogui.size()
            screen_center = (screen[0]/2,screen[1]/2)
            pyautogui.mouseDown(appCoor)
            pyautogui.dragTo(screen_center, duration=2)
        launcher.freeMode()
        '''

    @classmethod
    def tearDownClass(cls):
        pass
        #launcher.exitLauncher()

    def testMenuDock(self):
    	#launcher.menuDock(self.googleName)
    	#dockApps = Dock().getAllDockApps()
        sleep(2)
        self.assertEqual(1,10)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherAddToDock2('testMenuDock'))
        return suite

    
            
            

if __name__ == "__main__":
    runner.runTest(LauncherAddToDock2.suite())

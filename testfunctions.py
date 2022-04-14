# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:41:33 2022

@author: austi
"""
from pyunittest import UnitTest


class FirstTestClass:
    def __init__(self):
        self.className = self.__class__.__name__
    def beforeClass():
        print("This function should run once before any other function")
    
    def beforeEach():
        print("This functions should run before each test function")
        
    def testFunc():
        print("This is a test function")
        
    def afterEach():
        print("This function should run after each test function")
        
    def afterClass():
        print("This function should run after all test functions have run")
    
testClass = FirstTestClass()    
testObj = UnitTest()
#testObj.runTests()
testObj.runAllTestSuites()




    
    

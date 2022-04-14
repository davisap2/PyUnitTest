# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:22:55 2022

@author: Austin Davis
"""

from assertions.assertions import assertEquals

class TestSuiteTwo:
    def __init__(self):
        self.className = self.__class__.__name__
    def beforeClass():
        print("This function should run once before any other function")
    
    def beforeEach():
        print("This function should run before each test function")
        
    def testFunc():
        print("This is a test function")
        a = 2
        b = 2
        if assertEquals(a, b) == True:
            print('SUCCESS')
        else:
            print('FAILED')
        
    def afterEach():
        print("This function should run after each test function")
        
    def afterClass():
        print("This function should run after all test functions have run")
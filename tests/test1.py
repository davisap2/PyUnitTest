# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:21:23 2022

@author: Austin Davis
"""

from assertions.assertions import assertEquals

class TestSuiteOne:
    def __init__(self):
        self.className = self.__class__.__name__
    def beforeClass():
        print("This function should run once before any other function")
    
    def beforeEach():
        print("This function should run before each test function")
        
    def testFalseAssertEquals():
        a = 1
        b = 2
        return assertEquals(a,b)
    
    def testTrueAssertEquals():
        a = 2
        b = 2
        return assertEquals(a,b)
    
        
    def afterEach():
        print("This function should run after each test function")
        
    def afterClass():
        print("This function should run after all test functions have run")
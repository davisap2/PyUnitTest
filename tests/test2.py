# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:22:55 2022

@author: Austin Davis
"""

from assertions.assertions import assertEquals, assertTrue, assertFalse, assertNotNull, assertNull, assertArrayEquals

class TestSuiteTwo:
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
    
    def testTrueAssertTrue():
        a = True
        return assertTrue(a)
    
    def testFalseAssertTrue():
        a = False
        return assertTrue(a)
    
    def testTrueAssertFalse():
        a = False
        return assertFalse(a)
    
    def testFalseAssertFalse():
        a = True
        return assertFalse(a)
    
    def testTrueAssertNotNull():
        a = 1
        return assertNotNull(a)
    
    def testFalseAssertNotNull():
        a = None
        return assertNotNull(a)
    
    def testTrueAssertNull():
        a = None
        return assertNull(a)
    
    def testFalseAssertNull():
        a = 1
        return assertNull(a)
    
    def testTrueArrayEquals():
        a = [1, 2, 3]
        b = [1, 2, 3]
        return assertArrayEquals(a, b)
    
    def testFalseArrayEquals():
        a = [1, 2, 3]
        b = [1, 2, 4]
        return assertArrayEquals(a, b)
        
    def afterEach():
        print("This function should run after each test function")
        
    def afterClass():
        print("This function should run after all test functions have run")
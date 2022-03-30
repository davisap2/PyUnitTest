# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:41:27 2022

@author: Austin Davis
"""
import sys

from pyunitast.ast import parseAST

class UnitTest:
    def __init__(self, className):
        self.filepath = sys.argv[0] # filepath of test suite
        self.className = className
        self.functions = parseAST(self.filepath)
        
        print('CLASSNAME: ',self.className)
        #self.testClass = importModule.MyClass()
    def printFilepath(self):
        print(self.filepath)
        
    def printFunctions(self):
        print(self.functions)
        
    def runTests(self):
        setupFunctions = self.functions['setup']
        teardownFunctions = self.functions['teardown']
        testFunctions = self.functions['test']
        
        #beforeClass(setupFunctions)
        
        for test in testFunctions:
            beforeEach()
            passOrFail = runThisTest(test)
            #eval(self.testClass.test+'()') # runs the given function
            pass
        
        #afterClass(teardownFunctions)
    
    def runMethod(methodName):
        #run the given method here
        
        
        



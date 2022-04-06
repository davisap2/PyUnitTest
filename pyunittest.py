# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:41:27 2022

@author: Austin Davis
"""
import os, sys

from pyunitast.ast import parseAST
import tests.test1

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
        
    def runMethod(self, methodName):
        #run the given method here
        print("method Name: ", methodName+'()')
        eval(methodName+'()')
        
    def importClasses(self):
        testPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests\\') # directory of test suites
        print("path: ", testPath)
        print("__name__: ", __name__)
        
        # for each file in the tests folder, import the class inside them
        for py in [f[:-3] for f in os.listdir(testPath) if f.endswith('.py') and f != '__init__.py']:
            print("py: ", py)
            #mod = __import__('.'.join([__name__, py]), fromlist=[py])
            
            #mod = __import__('tests.'+py)
            mod = __import__('.'.join(['tests', py]), fromlist=[py])
            print("imported ", 'tests.'+py)
            
            for x in dir(mod):
                if isinstance(getattr(mod, x), type):
                    print("x: ", x)
            
            classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
            print("classes: ", classes)
            for cls in classes:
                print("a cls")
                setattr(sys.modules[__name__], cls.__name__, cls)
        
        
    def runTests(self):
        setupFunctions = self.functions['setup']
        teardownFunctions = self.functions['teardown']
        testFunctions = self.functions['test']
        
        self.importClasses()
        
        #beforeClass(setupFunctions)
        
        for test in testFunctions:
            print(test)
            #beforeEach()
            #passOrFail = runMethod(test)
            #self.runMethod(test)
            
            
        
        #afterClass(teardownFunctions)
    

        
        



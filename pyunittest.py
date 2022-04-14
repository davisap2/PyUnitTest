# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:41:27 2022

@author: Austin Davis
"""
import os, sys
import inspect

from pyunitast.ast import parseAST
import tests.test1

class UnitTest:
    
    def __init__(self):
        self.filepath = sys.argv[0] # filepath of test suite
        #self.className = className
        self.functions = parseAST(self.filepath)
        self.classList = []
        
        #print('CLASSNAME: ',self.className)
        #self.testClass = importModule.MyClass()
        
    def runMethod(self, classObj, methodName):
        #run the given method here
        print("method Name: ", methodName+'()')
        eval('classObj.'+methodName+'()')
        
    def importClasses(self):
        """
        This function will import all classes from all test files located in the tests folder.
        """
        testPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests\\') # directory of test suites
        #print("path: ", testPath)
        #print("__name__: ", __name__)
        
        # for each file in the tests folder, import the class inside them
        for py in [f[:-3] for f in os.listdir(testPath) if f.endswith('.py') and f != '__init__.py']:
            #print("py: ", py)
            #mod = __import__('.'.join([__name__, py]), fromlist=[py])
            
            #mod = __import__('tests.'+py)
            mod = __import__('.'.join(['tests', py]), fromlist=[py])
            print("imported ", 'tests.'+py)
            
            """
            for x in dir(mod):
                if isinstance(getattr(mod, x), type):
                    print("x: ", x)
            """
            
            classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
            self.classList.append(classes) #adding this class to list of all classes
            print("classes: ", classes)
            for cls in classes:
                print("cls: ", cls)
                setattr(sys.modules[__name__], cls.__name__, cls)
        
        print('CLASSLIST: ', self.classList)
        
        """
        for cls in self.classList:
            #print(cls[0].__name__)
            print(cls, ': ', inspect.getfile(cls[0]))
        """
        
    def runTests(self):
        setupFunctions = self.functions['setup']
        teardownFunctions = self.functions['teardown']
        testFunctions = self.functions['test']
        
        #import classes from test suite files
        self.importClasses()
        
        #beforeClass(setupFunctions)
        
        for test in testFunctions:
            print(test)
            #beforeEach()
            #passOrFail = runMethod(test)
            #self.runMethod(test)
            
            
        
        #afterClass(teardownFunctions)
        
    def getMethods(self, cls):
        """
        This function will get all the methods of the given class via AST parsing, then return them in a list.
        """
        print(cls, ': ', inspect.getfile(cls))
        thisFilepath = inspect.getfile(cls)
        methods = parseAST(thisFilepath)
        print('THESEMETHODS: ', methods)
        return methods
            
    def runAllTestSuites(self):
        """
        This method will run every test suite found in the tests folder.
        """
        self.importClasses()
        
        for cls in self.classList:
            print('CURRENT CLASS NAME: ', cls[0].__name__)
            className = cls[0].__name__
            classObj = globals()[className] # creates an instance of the given class
            methodList = self.getMethods(cls[0])
            
            self.beforeClass(classObj, methodList)
            
            for method in methodList['test']: #runs once for each test in the list
                self.beforeEach(classObj, methodList)
                self.runMethod(classObj, method) # runs current test
                self.afterEach(classObj, methodList)
                
            self.afterClass(classObj, methodList)
        
    def beforeClass(self, classObj, methodList):
        for method in methodList['setup']:
            if method == 'beforeClass':
                self.runMethod(classObj, method)
            
    def beforeEach(self, classObj, methodList):
        for method in methodList['setup']:
            if method != 'beforeClass':
                self.runMethod(classObj, method)
                
    def afterEach(self, classObj, methodList):
        for method in methodList['teardown']:
            if method != 'afterClass':
                self.runMethod(classObj, method)
                
    def afterClass(self, classObj, methodList):
        for method in methodList['teardown']:
            if method == 'afterClass':
                self.runMethod(classObj, method)
                
        

        
            

    

        
        



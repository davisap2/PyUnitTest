# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:07:53 2022

@author: Austin Davis
"""

import ast

def parseAST(filename):
    with open(filename) as file:
        code = file.read()
        tree = ast.parse(code)
        functions = getFunctions(tree.body)
        return functions
        
    
def getFunctions(body):
    testFunctions = []
    setupFunctions = []
    teardownFunctions = []
    classNames = []
    classes = [n for n in body if isinstance(n, ast.ClassDef)]
    
    for class_ in classes:
        classNames.append(class_)
        methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
        for method in methods:
            if (method.name[:4] == "test"):
                testFunctions.append(method.name)
            elif (method.name[:6] == 'before'):
                setupFunctions.append(method.name)
            elif (method.name[:5] == 'after'):
                teardownFunctions.append(method.name)
    """
    for f in body:
       #print(f)
        if (isinstance(f, ast.FunctionDef)):
            print("This is a function")
            if (f.name[:4] == "test"):
                testFunctions.append(f.name)
            elif (f.name[:6] == 'before'):
                setupFunctions.append(f.name)
            elif (f.name[:5] == 'after'):
                teardownFunctions.append(f.name)
    """
    
    functions = {
        "setup": setupFunctions,
        "test": testFunctions,
        "teardown": teardownFunctions
    }
    
    #return (f for f in body if isinstance(f, ast.FunctionDef)) 
    return functions

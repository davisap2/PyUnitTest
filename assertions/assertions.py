# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:49:28 2022

@author: Austin Davis
"""

from array import *
import test

def assertEquals(expected, actual):
  if expected == actual:
    return True
  return False

def assertTrue(expected):
  if expected == True:
    return True
  return False

def assertFalse(expected):
  if expected == False:
    return True
  return False

def assertNotNull(expected):
  if expected == None:
    return False
  return True

def assertNull(expected):
  if expected == None:
    return True
  return False

# assertSame and assertNotSame are not applicable here. 

def assertArrayEquals(expected, actual):
  for i in range(len(actual)):
    if actual[i] != expected[i]:
      return False
  return True

# PyUnitTest

A Python unit testing framework
=======

HOW TO DEPLOY: Simply run the pyunittest.py file.  This file creates an instance of the UnitTest class, then runs the runAllTestSuites() method.

If you would like to add any test suites to the system, insert them into the tests folder.

Test suite file names can be named anything you would like. Test suite files must contain only one class. No two test suite files can have the same class name within them.
All setup method names must start with "before." BeforeClass methods must be named beforeClass.
All teardown methods must start with "after." AfterClass methods must be named afterClass.
All test methods must start with "test."

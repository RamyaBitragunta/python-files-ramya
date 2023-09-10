
""" A module is a file in python that contains python code, usually with a specific functionality
or set of related functionalities
Modules allow you to organise your code into reusable units, making it easier to maintain, share and reuse code
across different projects.
You can import modules  into your python scripts or interactive sessions to access the functions,
classes and variables defined in them.
python package- module(we can reuse it).
Built-in modules
Importing specific items from a module

soon after we create a py package a dummy file wil be creataed
eg:- we have created pypackage and in  it __init__.py dummy file was created
What this file contains- lets go into __init__.py
"""

#____________________________________________________________________________________________

"""  MODULE PACKAGES
A PACKAGE IS SIMPLY A DIRECTORY CONTAINING PYTHON MODULE FILES AND A SPECIAL __init__py.file
 The __init__py.file can be empty or it may contain initialization code for the package.
 packages allow for logical grouping and prevent naming conflicts between modules.
 
 By including an __init__py.file in a package, you ensure that any necessary initialization code is executed when 
 the package is imported.
 
 The moment we put __init__py.file in an empty file it wil be converted into a package.
 #----------------------------------------------------------------------------------------------
 
 ALIASING MODULES
 import numpy as np
 arr = np.array([1,2,3,4,5])
 print(arr)
 output = [1,2,3,4,5]
"""
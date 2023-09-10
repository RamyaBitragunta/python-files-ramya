
# Module

"""
Instead of writing one big software in one file - we will break into small small parts
 For eg:- our project has 4 features ABCD -so we break down the components on paper and we will break it down
 into logical parts. After thinking we can make A and C can be one module., in the same way B and D in one module
 or we may break them into A, B, C, D ..and make them into 4 modules.. if we want to change anything in A
 it wont affect other modules.
 We can also reuse the modules- in next project
 In python one module may contains - variables, functions and classes
 one module wil be one file., so where we r doing a file here we have demo.py
 we can create another file as separate module."""

""" To create a separate module we will go into new and go for python file and we name this as 'calc'
-with many functions- and this may be separate module for us

Now if we want to use this calc module in another module called demo
modules may be of two types- inbuilt modules and own modules
For inbuilt- modules we can import modules or specific functions 
Bt it doesn't work for own modules like calc(own module)"""



# import Calc
# a = 7
# b = 5
# c = Calc.add(a,b) - we can say module name and dot add
# or we can use
# from Calc import add( or whatever function we want to call)
# and then we dont need to call Calc - it will simply work
# print(c)
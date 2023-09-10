# USE OF LAMBDA FUNCTION?

# Lambda function serves as nameless functions that are needed for very short period of time.
# To create short functions that takes less space, and that are used only once or twice in the code
# they are not stand-alone functions.
# a function in python without name- lambda function.

'''lambda function is very useful to write anonymous function.
used- in map functions,
lambda functions are also known as anonymous functions or  closure functions or single line functions.
name less functions or inline functions.
we can specify any number of parameters ;but only one expression
Result of expression can be assigned or stored in a variable'''
#lambda- its a keyword
#function name= x, a,b - parameters, operation/ expression(a+b)
# colons are used to separate parameters from expression.(only one expression should be present)

x = lambda a,b : a+b
print(x(1,2))
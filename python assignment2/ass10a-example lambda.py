# DISPLAY A STRING WITH PYTHON LAMBDA FUNCTION

str = "Hello world!"
(lambda str: print(str))(str)

# MULTIPLY 3 ARGUMENTS WITH LAMBDA FUNCTION
var = lambda i,j,k : i*j*k
print(var(4,5,6))

#maximum of two numbers with Lambda function
max_ = lambda a,b : a if (a>b) else b

print(max_(40,45))


#find square of a number with lambda function

squ_ = lambda i : i*i
print(squ_(3))
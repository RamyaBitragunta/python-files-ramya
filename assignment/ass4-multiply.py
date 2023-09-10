#TO MULTIPLY ALL THE NUMBERS IN A LIST- very imp

my_list= [4,6,8,10]
modi_list=[4*6*8*10]
print(modi_list)

#using- for loop - known as TRAVERSAL APPROACH
my_list= [4,6,8,10]
mul_ml= 1
for i in my_list:
    mul_ml= mul_ml*i

print("Answer is:",mul_ml)

#Another method- we have to install numpy package
#after insalling numpy package - we will get multiple methods frm this package
# import numpy
# my_list= [4,6,8,10]
# result=numpy.prod(my_list)
# print(result)

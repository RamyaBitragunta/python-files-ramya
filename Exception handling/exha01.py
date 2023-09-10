
# EXCEPTION HANDLING

# a = 5
# b = 0
#
# try:
#     print("resource open")
#     print(a/b)
# except Exception as e:
#     print("Hey you cannot divide a number by zero,",e)
#     print("resource closed")

#-----------------------------------------------------------------------------------------------

# a = 5
# b = 2
#
# try:
#     print("resource open")
#     print(a/b)
# except Exception as e:
#     print("Hey you cannot divide a number by zero,",e)
#
# finally:
#     print("resource closed")

#--------------------------------------------------------------------------------------------------------

# for different type of errors we have to use different except block

a = 6
b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except zeroDivisionError as e:
    print("hey you cannot divide any number by zero,",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("something went wrong")
finally:
    print("resource closed")


# in python except Exception as error: --(this is a parent block)
# exception block--this is handled by the python interpreter
#  but in Java it is done by-- Java virtual machine (JVM)
# when we dont know which type of errors occur we simply write - exception block
# however we use mostly the exception block in API automation.
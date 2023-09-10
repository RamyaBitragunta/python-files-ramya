
try:
    file = open('ramya_03','r')
    print(file.read())
    file.close()
except FileNotFoundError as error:
    print("File not found",error)

# error = e(the type of error) # its just a name of varaiable ,, we can give ramya also in place of error
# in line 7 , giving e or error after comma is not necessary, if want to give info about the error to user,
# then we can give.

# if we have exception ; then ideally close should  be in finally block .. bt as of now we havent kept in it.

try:
    file = open('ramya_03','r')
    print(file.read())
except FileNotFoundError as error:
    print("File not found",error)
finally:
    if file:
        file.close()


#  try block- the code which might throw error
#  except block - handling the error
#  finally block- no matter what(even if we get error or not) thisblock will execute.


""" Errors are problems in a program due to which the program will stop execution.
Exceptions are raised when some internal events occur which change the normal flow of program
several inbuilt-exceptions in python
Exception - it is the base class for all the built-in exceptions.
1.syntax error- this exception is raised when  the interpreter encounters a syntax error in the code
eg:- a misspelled word, a missing colon or an unbalanced parenthesis

2. Type error: This exception is raised when an operator or a function is applied to an object of wrong type.
such as adding a string to an integer

3. NameError -  this exception is raised when a variable or function name is not found in the current scope

4. IndexError - this exception is raised when an index is out of range for a list, tuple etc...

5. KeyError - this exception is raised when a key is not found in the dictionary

6. Value error:- this exception is raised when a function or method is called with an invalid argument or input,
such as trying to convert a string to an integer when the string doesnot represent a valid integer

7. Attribute error - this exception is raised when an attribute or method is not found on an object, such
as trying to access a non-existent attribute of a class instance

8. IOError - this exception is raised when an I/O operation, such as reading or writing a file,
fails due to an input/output error

9. ZeroDivisionError :- this exception is raised when an attempt is made to divide a number by zero

10. ImportError :- this exception is raised when an import statement fails to find or load a module

11. FileNotFoundError :- raised when a file or directory is requested but cannot found

12. IndentationError :- raised when there is an indentation related error, such as incorrect or inconsistent
indentation.

13. keyboardInterrupt : Raised when the user interrupts the execution of the program by pressing cntrl + C"""
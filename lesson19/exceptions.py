# reference for built-in exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp

# Define a custom exception by inheriting from the built-in Exception class
class JustNotCoolError(Exception):
    pass  # The 'pass' statement is used because we don't need to add anything else for now.

# Assign a value to variable x
x = 2

# try: 
#     print(x)
# except: 
#     print('An error occurred.')


# Start a try-except block to handle exceptions
try:
    # Manually raise a custom exception of type JustNotCoolError
    raise JustNotCoolError("This just isn't cool, man.")

    # The following lines are commented out, but they demonstrate different errors:

    # raise Exception("I'm a custom exception!")  # This raises a general Exception with a custom message.

    # print(x / 0)  # This would cause a ZeroDivisionError.

    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")  # This would raise a TypeError if x is not a string.

# Catch a NameError (e.g., when trying to use an undefined variable)
except NameError:
    print('NameError means something is probably undefined.')

# Catch a ZeroDivisionError (e.g., when attempting to divide by zero)
except ZeroDivisionError:
    print('Please do not divide by zero.')

# Catch any other exception (including the custom JustNotCoolError)
except Exception as error:
    print(error)  # Print the error message associated with the caught exception.

# This block executes if no exception occurs in the try block
else:
    print('No errors!')

# The finally block always executes, whether an error occurs or not
finally:
    print("I'm going to print with or without an error.")

# Function definition: Prints "Hello world!" when called
def hello_world():
    print("Hello world!")  

# Calling the hello_world function
hello_world()  

# Hello world!



# Function definition: Adds two numbers with default values of 0
def sum(num1=0, num2=0):
    # Checking if both inputs are integers, if not, return 0
    if (type(num1) is not int or type(num2) is not int):
        return 0
    # Returning the sum of num1 and num2
    return num1 + num2  

# Calling sum function with arguments 7 and 2, storing the result in 'total'
total = sum(7, 2)  
# Printing the result of the sum function
print(total)  

# 9



# Function definition: Accepts multiple positional arguments using *args
def multiple_items(*args):
    # Printing the tuple of arguments passed
    print(args)  
    # Printing the type of args, which is a tuple
    print(type(args))  

# Calling the function with multiple string arguments
multiple_items("Dave", "John", "Sara")  

# ('Dave', 'John', 'Sara')
# <class 'tuple'>



# Function definition: Accepts multiple keyword arguments using **kwargs
def mult_named_items(**kwargs):
    # Printing the dictionary of keyword arguments
    print(kwargs)  
    # Printing the type of kwargs, which is a dictionary
    print(type(kwargs))  

# Calling the function with named arguments
mult_named_items(first="Dave", last="Gray")  


# {'first': 'Dave', 'last': 'Gray'}
# <class 'dict'>
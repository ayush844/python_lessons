from functools import reduce  # Importing reduce function

# --------------------------- LAMBDA FUNCTION ---------------------------
# A lambda function is an anonymous, single-line function defined using the 'lambda' keyword.
# It can take multiple arguments but only contains a single expression.
# Syntax: lambda arguments: expression
# Example: lambda num: num * num  (Returns the square of num)

# Regular function to square a number

# squared = lambda num: num * num
# print(squared(2) 

def squared(num): return num * num
# Equivalent lambda function: lambda num: num * num

print(squared(2))  # Output: 4

# Regular function to add 2 to a number
def add_two(num): return num + 2
# Equivalent lambda function: lambda num: num + 2

print(add_two(12))  # Output: 14

# Regular function to sum two numbers

# sum_total = lambda a, b: a + b

def sum_total(a, b): return a + b
# Equivalent lambda function: lambda a, b: a + b

print(sum_total(10, 8))  # Output: 18



# --------------------------- HIGHER-ORDER FUNCTION ---------------------------
# A higher-order function is a function that:
# 1. Takes another function as an argument, OR
# 2. Returns a function as its output.
# These functions enable functional programming concepts like function composition.

def funcBuilder(x):
    """
    This function returns a lambda function that adds 'x' to its input.
    """
    return lambda num: num + x  # Returns a function that adds 'x' to 'num'

# Creating functions dynamically
add_ten = funcBuilder(10)  # Returns a function that adds 10
add_twenty = funcBuilder(20)  # Returns a function that adds 20

print(add_ten(7))    # 7 + 10 = 17
print(add_twenty(7)) # 7 + 20 = 27

# --------------------------- FUNCTIONAL PROGRAMMING WITH MAP, FILTER, AND REDUCE ---------------------------

numbers = [3, 7, 12, 18, 20, 21]

# Using map() with a lambda function to square each number in the list

# map(function, iterable) applies 'function' to each item in 'iterable'
squared_nums = map(lambda num: num * num, numbers)
# Equivalent to: [num * num for num in numbers]

print(list(squared_nums))  # Output: [9, 49, 144, 324, 400, 441]



# Using filter() to keep only odd numbers

# filter(function, iterable) keeps elements where 'function' returns True
odd_nums = filter(lambda num: num % 2 != 0, numbers)
# Equivalent to: [num for num in numbers if num % 2 != 0]

print(list(odd_nums))  # Output: [3, 7, 21]



numbers = [1, 2, 3, 4, 5, 1]

# Using reduce() to compute the sum of numbers, starting with an initial value of 10

# reduce(function, iterable, initial_value) applies 'function' cumulatively to elements
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
# Equivalent to: sum(numbers, 10)

print(total)  # Output: 26 (10 + 1 + 2 + 3 + 4 + 5 + 1)

print(sum(numbers, 10))  # Built-in sum function with an initial value of 10



names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

# Using reduce() to count total characters in all names
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
# Equivalent to: sum(len(name) for name in names)

print(char_count)  # Output: Total number of characters in all names

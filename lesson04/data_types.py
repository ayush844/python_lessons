import math


# String data type

# literal assignment

first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

#       <class 'str'>
#       True
#       True


print("---------------------------------------------------------------------------------------------")


# constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

#   <class 'str'>
#   True
#   True




# Concatenation
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

#   Dave Gray
#   Dave Gray!




# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

#   <class 'str'>
#   1980



statement = "I like rock music from the " + decade + "s."
print(statement)

#   I like rock music from the 1980s.



# Multiple lines
multiline = '''
Hey, how are you?                                   

I was just checking in.    
                                All good?

'''
print(multiline)


# Hey, how are you?                                   

# I was just checking in.    
#                                 All good?




# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#   Where's this at\located?


print("---------------------------------------------------------------------------------------------")


# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                        "
multiline = "                  " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")


#  RESULTS:

# Dave
# dave
# DAVE
# Dave

# Hey, How Are You?                                   

# I Was Just Checking In.    
#                                 All Good?



# Hey, how are you?                                   

# I was just checking in.    
#                                 All ok?



# Hey, how are you?                                   

# I was just checking in.    
#                                 All good?


# 126
# 184
# 123
# 165
# 142




print("---------------------------------------------------------------------------------------------")



# Build a menu
title = "menu".upper()  # Converts the string "menu" to uppercase: "MENU".

print(title.center(20, "="))  # Centers the string "MENU" in a field of 20 characters, padding with "=" on both sides.

print("Coffee".ljust(16, ".") + "$1".rjust(4))  # Left-justifies "Coffee" in a field of 16 characters, filling extra space with ".", and right-justifies "$1" in a field of 4 characters.

print("Muffin".ljust(16, ".") + "$2".rjust(4))  # Left-justifies "Muffin" in a field of 16 characters, filling extra space with ".", and right-justifies "$2" in a field of 4 characters.

print("Cheesecake".ljust(16, ".") + "$4".rjust(4))  # Left-justifies "Cheesecake" in a field of 16 characters, filling extra space with ".", and right-justifies "$4" in a field of 4 characters.


#   ========MENU========
#   Coffee..........  $1
#   Muffin..........  $2
#   Cheesecake......  $4


print("")

# String index values
print(first[1])  # Accesses the character at index 1 (second character) of the string `first`.
print(first[-1])  # Accesses the last character of the string `first`.
print(first[1:-1])  # Accesses the substring starting from index 1 up to (but not including) the last character of the string `first`.
print(first[1:])  # Accesses the substring starting from index 1 to the end of the string `first`.

# Some methods return boolean data
print(first.startswith("D"))  # Returns `True` if the string `first` starts with the character "D"; otherwise, `False`.
print(first.endswith("Z"))  # Returns `True` if the string `first` ends with the character "Z"; otherwise, `False`.


#   a
#   e
#   av
#   ave
#   True
#   False



print("---------------------------------------------------------------------------------------------")

# ljust and rjust:


#  ljust

print("Hello".ljust(10, "-"))  # Output: "Hello-----"
# "Hello" is left-aligned in a space of 10 characters, and "-" fills the extra space.

print("Python".ljust(15, "*"))  # Output: "Python**********"
# "Python" stays on the left, and "*" fills the space to make the total width 15.

print("Hi".ljust(5))  # Output: "Hi   "
# No fill character specified, so it defaults to spaces ("Hi   ").



#  rjust

print("Hello".rjust(10, "-"))  # Output: "-----Hello"
# "Hello" is right-aligned in a space of 10 characters, and "-" fills the extra space on the left.

print("Python".rjust(15, "*"))  # Output: "**********Python"
# "Python" moves to the right, and "*" fills the space to make the total width 15.

print("Hi".rjust(5))  # Output: "   Hi"
# No fill character specified, so it defaults to spaces ("   Hi").


print("---------------------------------------------------------------------------------------------")


# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# <class 'bool'>
# True


# Numeric data types


# integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# <class 'int'>
# True


# float type

gpa = 3.28
y = float(1.14)
print(type(gpa))

#  <class 'float'>


# complex type

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#   <class 'complex'>
#   5.0
#   3.0


# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

# 3.28
# 3.28

print(round(gpa))
print(round(gpa, 1))

# 3
# 3.3

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# 3.141592653589793
# 8.0
# 4
# 3


# Casting a string to a number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#  <class 'int'>

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
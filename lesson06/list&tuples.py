# - **List**: A mutable, ordered collection of items. Items can be added, removed, or changed. Defined using square brackets (`[]`).  
#   **Example**: `my_list = [1, 2, 3]`

# - **Tuple**: An immutable, ordered collection of items. Items cannot be changed after creation. Defined using parentheses (`()`).  
#   **Example**: `my_tuple = (1, 2, 3)`





users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in users)

print("Dave" in emptylist)

print(users[0])

print(users[-2])

print(users.index('Sara'))

# True
# False
# Dave
# John
# 2


print(users[0:2])
print(users[1:])
print(users[-3:-1])

# ['Dave', 'John']
# ['John', 'Sara']
# ['Dave', 'John']

print(len(data))

# 3

users.append('Elsa')
print(users)
# ['Dave', 'John', 'Sara', 'Elsa']

######################################################################################################

# add a new list to an existing list

# 1rst way
users += ['Jason']
print(users)
# ['Dave', 'John', 'Sara', 'Elsa', 'Jason']


# users += 'Jason'
# print(users)
# # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n']


# 2nd way
users.extend(['Robert', 'Jimmy'])
print(users)
# ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# users.extend(data)
# print(users)
# # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy', 'Dave', 42, True]

############################################################################################################

# insert an element at a specific index


users.insert(0, 'Bob')  #insert something at very first position
print(users)
#  ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

users[2:2] = ['Eddie', 'Alex']  # insert something at 3rd position [begin at 2nd index, end at 2nd index]
print(users)
# ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

users[1:3] = ['Robert', 'JPJ']  # replace 2nd and 3rd position
print(users)
# ['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']


#######################################################################################################

users.remove('Bob')
print(users)

# ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

print(users.pop())

# Jimmy

print(users)

# ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

del users[0]
print(users)

# ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']


# del data      # data will be deleted

data.clear()    # data will be empty
print(data)
# []


# users =>  ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

users[1:2] = ['dave']
users.sort()
print(users)
['Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'dave']
# dave is at end because lower case, comes after upper case

# to put dave in correct order:
users.sort(key=str.lower)
print(users)
# ['dave', 'Elsa', 'Jason', 'John', 'JPJ', 'Robert', 'Sara']


nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
#[5, 1, 78, 42, 4]

# nums.sort(reverse=True)
# print(nums)
# # [78, 42, 5, 4, 1]


#  all the sort method we used modifies the original list, if we want to keep the original list, we can use the sorted function
#  sorted function will return a new list, and original list will remain unchanged

print(sorted(nums, reverse=True))
print(nums)
# [78, 42, 5, 4, 1]


# we can also copy our original list, there are 3 ways to copy a list

# 1. by using copy method
numscopy = nums.copy()

# 2. by using list function
mynums = list(nums)

# 3. by using slicing
mycopy = nums[:]



print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# [5, 1, 78, 42, 4]
# [5, 1, 78, 42, 4]
# [1, 4, 5, 42, 78]
# [5, 1, 78, 42, 4]

print(type(nums))
#  <class 'list'>

mylist = list([1, "Neil", True])
print(mylist)
#  [1, 'Neil', True]


################################################################################################
################################################################################################
################################################################################################


# Tuples

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# ('Dave', 42, True)
# <class 'tuple'>
# <class 'tuple'>

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)
# ('Dave', 42, True, 'Neil')

# unpacking a tuple
(one, *two, hey) = anothertuple # *two will take all the values except the first and last
print(one)
print(two)
print(hey)

# 1
# [4, 2, 8, 2]
# 2

print(anothertuple.count(2))
# 3

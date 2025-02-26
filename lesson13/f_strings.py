person = "Dave"
coins = 3

#################
# Concatenating strings (Traditional way)
# Using the `+` operator requires explicit type conversion for non-string values
print("\n" + person + " has " + str(coins) + " coins left.")

# Dave has 3 coins left.


#################
# Using the old `%` formatting method (C-style string formatting)
# `%s` is a placeholder for strings and other data types
message = "\n%s has %s coins left." % (person, coins)
print(message)

# Dave has 3 coins left.


#################
# Using `.format()` method (More flexible than `%` formatting)
# `{}` acts as a placeholder, and `.format()` fills them in order
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# Dave has 3 coins left.


# You can also specify positions inside `{}` to change the order
message = "\n{1} has {0} coins left.".format(coins, person)  # Swapped positions
print(message)

# Dave has 3 coins left.


# Using named placeholders inside `.format()`
message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)

# Dave has 3 coins left.


# You can also unpack a dictionary into `.format()`
player = {'person': 'Dave', 'coins': 3}
message = "\n{person} has {coins} coins left.".format(**player)  # Unpacking dictionary
print(message)



##################
# f-Strings! (Introduced in Python 3.6 - Most modern and recommended way)

# f-strings allow embedding expressions directly inside curly braces `{}`.
message = f"\n{person} has {coins} coins left."
print(message)

# Dave has 3 coins left.


# You can include expressions inside f-strings
message = f"\n{person} has {2 * 5} coins left."  # Evaluates 2 * 5
print(message)

# Dave has 10 coins left.


# You can use string methods inside f-strings
message = f"\n{person.lower()} has {2 * 5} coins left."  # `person.lower()` makes "Dave" lowercase
print(message)

# dave has 10 coins left.


# You can also access dictionary values inside f-strings
message = f"\n{player['person']} has {2 * 5} coins left."  # Fetching value from dictionary
print(message)

# Dave has 10 coins left.



##################
# Formatting numbers inside f-strings

num = 10
# `:.2f` formats the number to 2 decimal places
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# 2.25 times 10 is 22.50


# Looping with f-strings
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")  # Multiplies and formats to 2 decimal places

# 2.25 times 1 is 2.25
# 2.25 times 2 is 4.50
# 2.25 times 3 is 6.75
# 2.25 times 4 is 9.00
# 2.25 times 5 is 11.25
# 2.25 times 6 is 13.50
# 2.25 times 7 is 15.75
# 2.25 times 8 is 18.00
# 2.25 times 9 is 20.25
# 2.25 times 10 is 22.50



# Percentage formatting with f-strings
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")  # `:.2%` formats as a percentage with 2 decimal places

# 1 divided by 4.52 is 22.12%
# 2 divided by 4.52 is 44.25%
# 3 divided by 4.52 is 66.37%
# 4 divided by 4.52 is 88.50%
# 5 divided by 4.52 is 110.62%
# 6 divided by 4.52 is 132.74%
# 7 divided by 4.52 is 154.87%
# 8 divided by 4.52 is 176.99%
# 9 divided by 4.52 is 199.12%
# 10 divided by 4.52 is 221.24%
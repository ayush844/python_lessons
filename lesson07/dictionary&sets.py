# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))


# {'vocals': 'Plant', 'guitar': 'Page'}
# {'vocals': 'Plant', 'guitar': 'Page'}
# <class 'dict'>
# 2


print("//////////////////////////////////////////////////////////////////////////")

# Access items
print(band["vocals"])
print(band.get("guitar"))

# Plant
# Page


# list all keys
print(band.keys())

# dict_keys(['vocals', 'guitar'])


# list all values
print(band.values())

# dict_values(['Plant', 'Page'])


# list of key/value pairs as tuples
print(band.items())

# dict_items([('vocals', 'Plant'), ('guitar', 'Page')])


# verify a key exists
print("guitar" in band)
print("triangle" in band)

# True
# False


# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}


# Remove items
print(band.pop("bass"))
print(band)

# JPJ
# {'vocals': 'Coverdale', 'guitar': 'Page'}


band["drums"] = "Bonham"
print(band)

# {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}


print(band.popitem())  # returns a tuple
print(band)

# ('drums', 'Bonham')
# {'vocals': 'Coverdale', 'guitar': 'Page'}


print("///////////////////////////////////////////////////////////////////////////////////////////////")


# Delete and clear

band["drums"] = "Bonham"
del band["drums"]  # Removes the 'drums' key and its associated value from the 'band' dictionary.
print(band)  # Prints the updated 'band' dictionary after deletion.

# {'vocals': 'Coverdale', 'guitar': 'Page'}

band2.clear()  # Removes all key-value pairs from the 'band2' dictionary, making it empty.
print(band2)  # Prints the now-empty 'band2' dictionary.

# {}

del band2  # Deletes the 'band2' dictionary from memory.


print("///////////////////////////////////////////////////////////////////////////////////////////////")


# Copy dictionaries

# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# # Bad copy!
# # {'vocals': 'Coverdale', 'guitar': 'Page'}
# # {'vocals': 'Coverdale', 'guitar': 'Page'}

# band2["drums"] = "Dave"
# print(band)

# # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

# -------------------------------------------------------------------------------------------

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# Good copy!
# {'vocals': 'Coverdale', 'guitar': 'Page'}
# {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}


# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Good copy!
# {'vocals': 'Coverdale', 'guitar': 'Page'}

print("///////////////////////////////////////////////////////////////////////////////////////////////")

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"])
print(band["member1"]["name"])

# {'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
# {'name': 'Plant', 'instrument': 'vocals'}
# Plant

print("///////////////////////////////////////////////////////////////////////////////////////////////")

# Sets


nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# {1, 2, 3, 4}
# {1, 2, 3, 4}
# <class 'set'>
# 4


# Sets are unordered, so you cannot refer to an element in a set with an index position or a key.

# No duplicate allowed

nums = {1, 2, 2, 3}
print(nums)
# {1, 2, 3}

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# {False, 1, 2, 3, 4}

# check if a value is in a set
print(2 in nums)

# True

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# {False, 1, 2, 3, 4, 8}


# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# {False, 1, 2, 3, 4, 5, 6, 7, 8}


# you can use update with lists, tuples, and dictionaries, too, means we don't need to pass morenums as aset we can use morenums as set, list , tuple or dictionary and update will stll work here.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)
# {1, 2, 3, 5, 6, 7}


#🔹 Use .update() when you want to modify the original set.
#🔹 Use .union() when you need a new set without changing the original.



# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# {2, 3}


# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)

# {1, 4}
import os
# r = Read
# a = Append
# w = Write
# x = Create


# initial text in all 3 files(names.txt, more_names.txt, context.txt):
# Dave
# Jane
# Eddie
# Jimmie

#############################################################################################

# Read - error if it doesn't exist

f = open("names.txt")


# print(f.read())

# # Dave
# # Jane
# # Eddie
# # Jimmie



# print(f.read(2))

# # Da (first 2 characters of the file)



# print(f.readline())
# print(f.readline())

# # Dave

# # Jane



# for line in f:
#     print(line)

# # Dave

# # Jane

# # Eddie

# # Jimmie    



f.close() # close the file

#############################################################################################



# try:
#     f = open("names.txt")
#     print(f.read())
# except:
#     print("The file you want to read doesn't exist")
# finally:
#     f.close()

# # Dave
# # Jane
# # Eddie
# # Jimmie    


#############################################################################################


# # Append - creates the file if it doesn't exist

# f = open("names.txt", "a")
# f.write("Neil\n")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# # Dave
# # Jane
# # Eddie
# # JimmieNeil


#############################################################################################


# # Write (overwrite)
# f = open("context.txt", "w")
# f.write("I deleted all of the context")
# f.close()

# f = open("context.txt")
# print(f.read())
# f.close()

# # I deleted all of the context


#############################################################################################

import os  # Importing os module to check file existence and remove files

# Two ways to create a new file

# Method 1: Using "w" (write mode)
# Opens a file for writing. If the file does not exist, it creates it.
# If the file exists, it overwrites its content.
f = open("name_list.txt", "w")
f.close()  # Always close the file after opening it

# Method 2: Using "x" (exclusive creation mode)
# Creates the file only if it does not already exist.
# If the file exists, it raises a FileExistsError.
if not os.path.exists("dave.txt"):  # Checking if the file already exists
    f = open("dave.txt", "x")  # "x" mode ensures the file is created if it doesn't exist
    f.close()  # Closing the file after creation


#############################################################################################

# Delete a file

# Check if the file exists before trying to delete it
if os.path.exists("dave.txt"):  
    os.remove("dave.txt")  # Deletes the file
else:
    print("The file you wish to delete does not exist")  # Avoids an error if the file is missing

# Using "with open()" for better file handling

# This ensures that the file is properly closed after reading, even if an error occurs.
with open("more_names.txt") as f:  
    content = f.read()  # Read the entire content of "more_names.txt"

# Writing content to another file
# "w" mode creates the file if it doesn't exist or overwrites it if it does.
with open("names.txt", "w") as f:  
    f.write(content)  # Writes the content of "more_names.txt" into "names.txt"


# The with statement ensures the file is closed properly after reading, but it does not limit the scope of variables declared inside it.
# The variable content is still accessible after the first with open() block because it was declared in the main script scope.

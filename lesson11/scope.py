# Global variables (accessible anywhere in the script)
name = "Dave"
count = 1  # Global variable 'count'

def another():
    # Local variable 'color' (only accessible inside 'another' function)
    color = "blue"
    
    # 'global' keyword allows modification of the global 'count' variable
    global count  
    count += 1  # Increments the global 'count' by 1
    print(count)  # Prints updated 'count' value

    def greeting(name):
        # 'nonlocal' allows modifying 'color' from the outer function 'another'
        nonlocal color  
        color = "red"  # Modifies the 'color' variable from 'another'
        print(color)  # Prints updated color (red)
        print(name)  # Prints the passed argument (e.g., "Dave")

    # Calling the nested function with "Dave" as an argument
    greeting("Dave")

# Calling the function 'another'
another()


# 2
# red
# Dave
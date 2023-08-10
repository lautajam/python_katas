"""Jenny has written a function that returns a greeting 
for a user. However, shes in love with Johnny, and would 
like to greet him slightly different. She added a 
special case to her function, but she made a mistake.
Can you help her?"""

# Original function
def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"

# Fix
# The error was an if below the first return, it never got to check the condition
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# MAIN
print(greet(input("Type any name, please: ")))
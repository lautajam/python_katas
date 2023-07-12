"""Given a string, write a function that returns the 
string with a question mark ("?") appends to the 
end, unless the original string ends with a question 
mark, in which case, returns the original string."""

# Adds a ? to the string if there is no ? at the end
def ensure_question(string):
    return string if (string[len(string) - 1] == "?") else string + "?"

# MAIN

print(ensure_question("Hello World"))
print(ensure_question("Hello World?"))
print(ensure_question("Hel?lo World"))
print(ensure_question("Hello? World?"))
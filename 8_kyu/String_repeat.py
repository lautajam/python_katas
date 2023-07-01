"""Write a function that accepts an integer n and a string s 
as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> 'IIIIII'
5, "Hello" -> 'HelloHelloHelloHelloHello'"""

# Repeat n (number) times a letters group 
def repeat_str(letters, number):
    phrase = ""
    for var in range(0, number):
        phrase += letters
    return phrase

# MAIN

print(repeat_str("hola", 5))
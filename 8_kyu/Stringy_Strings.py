"""
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""

# writes as many 1's and 0's as the number entered, alternating between them.
def stringy_string(size):
    result = ""
    for number in range(0, size):
        if number % 2 == 0:
            result += "1"
        else:
            result += "0"
    return result

# MAIN
print(stringy_string(6))
print(stringy_string(4))
print(stringy_string(12))
""""Pits" and "lands" are physical features on the surface of a CD 
that represent binary data. Pits are small depressions or grooves 
on the surface of the CD, while lands are flat areas between two 
adjacent pits.

The pits and lands themselves do not directly represent the zeros 
and ones of binary data. Instead, Non-return-to-zero, inverted encoding 
is used: a change from pit to land or land to pit indicates a one, 
while no change indicates a zero.

In this Kata, you should implement a function, that takes integer 
in range [0..255] (8 bits), and returns combination of pits and lands 
that encode the number. Result should have format of string: PLLPL... 
where P represents pit and L represents land. Combination should always 
start with pit. Numbers should be encoded in little-endian, which means 
you start from least significant bit.

Example
Input: 5
Binary representation (8 bits): 00000101
Output: PLLPPPPPP

Explanation:
Starts from P as per description
Changes to L because first bit is 1
Stays L because second bit is 0
Changes to P because third bit is 1
Stays P because fourth bit is 0
Stays P till the end because all subsequent bits are 0"""

# FUNCTIONS

# Converts number int in binary list
def convert_binary(number):
    binary = [0]
    # Gives the binary digit and gives the new number that gives a other binary digit
    while number != 0:
        binary.append(number % 2)
        number = int(number / 2)
    # Add the missing 0
    if len(binary) < 9:
        for var in range (1, (9 - len(binary))):
            binary.insert(0, 0)
    return binary

# Transform the binary number to encode data cd
def encode_data(binary):
    encode_dt, ant, letter = "P", "L", "P"
    binary.reverse()
    # P if the number is the same or L if the number is different.
    for num in binary:
        if num == 1:
            letter, ant = ant, letter
            encode_dt += letter
        else:
            encode_dt += letter
    return encode_dt

# MAIN

number = int(input("Ingrese un numero entre [0  y 255] por favor: "))

# Checks if the number is within  the range
if number not in range(0, 256):
    go = False
    while number not in [0, 255]:
        number = int(input("Ingrese un numero entre [0  y 255] por favor: "))

print(convert_binary(number))

print(encode_data(convert_binary(number)))

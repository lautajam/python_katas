# In this simple exercise, you will build a program that takes a value, integer, 
# and returns a list of its multiples up to another value, limit . If limit is a 
# multiple of integer, it should be included as well. 
# There will only ever be positive integers passed into the function, not consisting of 0. 
# The limit will always be higher than the base.

# For example, if the parameters passed are (2, 6), 
# the function should return [2, 4, 6] as 2, 4, 
# and 6 are the multiples of 2 up to 6.

# In range of frist and last number try all numbers if the rest between num/f_num = 0 and save the number

# Check if f_num > l_num and change the values
def check_position(f_number, l_number):
    if f_number > l_number:
        f_number, l_number = l_number, f_number
    return f_number, l_number

def mult(f_number, l_number):
    multiples = []
    f_number, l_number = check_position(f_number, l_number)
    for number in range(f_number, l_number + 1):
        if (number % f_number) == 0:
            multiples.append(number)
    return multiples

# check if number isn´t 0
def validation(number):
    if number == 0:
        go = False
        while go:
            print("0 isn´t allowed, try with other number")
            number = int(input("Type a number, please: "))
            if number != 0:
                go = True
    return number

# MAIN

f_number = int(input("Type a first range number, please: "))
f_number = validation(f_number)
l_number = int(input("Type a last range number, please: "))
l_number = validation(l_number)

multiples = mult(f_number, l_number)

print(multiples)
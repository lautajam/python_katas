"""This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""

# Takes the letters str and returns a new str with each letter written times the number of it's position
def accum(letters):
    position, letters_final = 0, ""
    for letter in letters:
        position += 1
        for var in range(0, position):
            if var == 0: letters_final += letter.upper()
            else: letters_final += letter.lower()
        letters_final += "-"
    return letters_final[:-1]

# MAIN

print(accum(letters="jhksdbg"))
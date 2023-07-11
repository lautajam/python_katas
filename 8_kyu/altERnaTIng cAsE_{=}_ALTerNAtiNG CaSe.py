"""altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define String.prototype.toAlternatingCase (or a similar function/method such 
as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language
; see the initial solution for details) such that each lowercase letter becomes 
uppercase and each uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
As usual, your function/method should be pure, i.e. it should not mutate the original string."""

# Takes a input and return each lowercase letter becomes uppercase and each uppercase letter becomes lowercase
def toAlternatingCase(string):
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    new_string = ""

    for element in string:
        if element in lower_letters:
            new_string += element.upper()
        elif element in upper_letters:
            new_string += element.lower()
        else:
            new_string += element
    
    return new_string

# MAIN

print(toAlternatingCase(string="hello world"))
print(toAlternatingCase(string="1a2b3c4d5e"))
print(toAlternatingCase(string="HeLLo WoRLD"))
print(toAlternatingCase(string="12345"))
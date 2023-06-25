"""Write a function that checks if a given string (case insensitive) 
is a palindrome. A palindrome is a word, number, phrase, or other 
sequence of symbols that reads the same backwards as forwards, such 
as madam or racecar, the date and time 12/21/33 12:21, and the sentence: 
'A man, a plan, a canal - Panama'."""

# list with symbols to check
symbols = ['!', "¡", '"', '#', '$', '%', '&', "'",
                         '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '¿', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', " "]

# Extracts all the Symbols from the sentence and makes it lowercase
def clean_phrase(phrase):
    for element in phrase:
        if element in symbols:
            phrase = phrase.replace(element, "")
    return phrase.lower()

# Takes the phrase and transforms it into a list and an inverse list and checks item by item if both are equal
def is_palindrome(phrase):

    phrase_list = list(phrase)
    phrase_list_inverse = phrase_list[::-1]

    is_pal = True
    for index in range(0, len(phrase_list)):
        if phrase_list[index] != phrase_list_inverse[index]:
            is_pal = False
            break
    return is_pal

# MAIN

phrase = clean_phrase(input("Type a phrase palindrome: "))

if is_palindrome(phrase): print(phrase, "is a palindrome")
else: print(phrase, "isn't a palindrome")
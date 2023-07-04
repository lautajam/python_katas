"""Create a function called shortcut to remove the lowercase vowels 
(a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
don't worry about uppercase vowels
y is not considered a vowel for this kata"""

# Takes a word, removes the vowels and returns the word without vowels 
def vowels_remover(word): 
    word_new = ""
    for letter in word:
        if letter in ["a", "e", "i", "o" ,"u"] : pass
        else: word_new += letter
    return word_new

# MAIN

print(vowels_remover(word="Hi! This sentence is for testing the code."))
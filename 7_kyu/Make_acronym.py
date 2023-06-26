"""Write function which takes a string and make an acronym of it.

Rule of making acronym in this kata:

split string to words by space char
take every first letter from word in given string
uppercase it
join them toghether
Eg:

Code wars -> C, w -> C W -> CW
Note: There will be at least two words in the given string!"""

# Takes a phrase and makes a acronym with the first letter of each word
def make_acronym(phrase):
    phrase_list = phrase.split(" ")
    acronym = ""
    for letter in phrase_list:
        acronym += letter[0]
    return acronym.upper()

# MAIN
print(make_acronym(phrase="i'm a test"))

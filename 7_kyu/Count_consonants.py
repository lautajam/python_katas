"""Complete the function that takes a string of English-language text 
and returns the number of consonants in the string.
Consonants are all letters used to write English excluding 
the vowels a, e, i, o, u."""

# Count consonants checking letter by letter of word/str
def count_consonants(sentence):

    consonats = "bcdfghjklmnñpqrstvwxyz" # Str with consonants
    count_cons = 0

    # Check letter by letter if a consonats and adds 1 to count
    for letter in sentence: 
        if letter.lower() in consonats and letter != " ": count_cons += 1

    return count_cons

# MAIN

print(count_consonants(sentence="This is a test"))
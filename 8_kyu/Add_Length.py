# What if we need the length of the words separated by a space 
# to be added at the end of that same word and have it returned 
# as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]

# Your task is to write a function that takes a String and returns 
# an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always 
# be separated by a space.

# Take a text and separate it into each space and add all the words its length
def words_lenth(text):
    
    list_words = []

    for word in text.split(" "): 
        list_words.append(word + " " + str(len(word)))

    return list_words

# MAIN

text = input("Type a text (all words separate with space): ")

list_words = words_lenth(text)

print(list_words)


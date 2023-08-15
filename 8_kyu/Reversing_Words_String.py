"""
You need to write a function that reverses the words in a given string. 
A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""

# Reverse string
def reversing_words(text):
    text_list = text.split(" ")
    text_inverse = ""
    for index in range(len(text_list) - 1, -1, -1):
        text_inverse += text_list[index] + " "
    return text_inverse

# MAIN
print(reversing_words("Hello World!"))
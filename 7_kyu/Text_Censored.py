"""
The exercise consists of creating a function called "censored" that takes two arguments: "text" 
and "word". The function must censor all occurrences of the word "word" in the text "text" with asterisks (*).

For example, if we call the function with the following text and word:

Text: "Internet censorship is a controversial and sensitive topic."
Word: "censorship"

The function should return:

"******* on the Internet is a controversial and sensitive topic."

The purpose of this function is to hide a specific word in a given text and display 
it censored to respect privacy or avoid sensitive content."""

# censors a given word from a given text
def censored(text, word):
    new_text = ""
    censure = ""
    for _ in word:
        censure += "*"
    for word_text in text.split(" "):
        if word_text.lower() == word.lower():
            new_text += censure + " "
        else:
            new_text += word_text + " "
    return new_text

print(censored("Hola mundo hola perro hola salchicha", "hola"))
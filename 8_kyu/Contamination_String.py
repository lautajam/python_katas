"""An AI has infected a text with a character!!

This text is now fully mutated to this character.

If the text or the character are empty, return an empty string.
There will never be a case when both are empty as nothing is going on!!

Note: The character is a string of length 1 or an empty string.

Example
text before = "abc"
character   = "z"
text after  = 'zzz'"""

# Replace all character with the char selected, just leave the spaces
def contam_string(text, char):
    text_after = ""
    for character in text:
        if character == " ": text_after += " "
        else: text_after += char
    return text_after

# MAIN
text = "This text is a test to the code"

print(text + "\n" + contam_string(text, "z"))
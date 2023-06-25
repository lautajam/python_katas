"""You are going to be given a word. Your job is to return the middle 
character of the word. If the word's length is odd, return the middle 
character. If the word's length is even, return the middle 2 characters.

#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"

#Input
A word (string) of length 0 < str < 1000 (In javascript you may get 
slightly more than 1000 in some test cases due to an error in the test cases). 
You do not need to test for this. This is only here to tell you that you do not 
need to worry about your solution timing out.

#Output
The middle character(s) of the word represented as a string."""

# If the word lenght is even gives the two middle characters, if odd gives the middle character
def get_middle_cha(word):
    middle = ""
    if len(word) % 2 == 0:
        middle = word[int(len(word)/2) - 1] + word[int(len(word)/2)]
    else:
        middle = word[int(len(word)/2)]

    return middle

# MAIN 
word = input("Type a word: ")
print("The '" + word + "' middle(s) character(s):", get_middle_cha(word))

print(get_middle_cha("test"))
print(get_middle_cha("testing"))
print(get_middle_cha("middle"))
print(get_middle_cha("A"))

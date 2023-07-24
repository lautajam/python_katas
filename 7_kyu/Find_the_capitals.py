"""Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes 
of all capital letters in the string."""

def SearchCapitals(word):

    capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    capitals_index = []

    for letter in word:
        if letter in capitals:
            capitals_index.append(word.index(letter))

    return capitals_index


print(SearchCapitals('CodEWaRs')) # ---> [0, 3, 4, 6]
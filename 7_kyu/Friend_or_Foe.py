"""DESCRIPTION:
Make a program that filters a list of strings and returns 
a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that 
it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output."""

# Checks a list of people to see if they have friends on it by the length of each name
def shouldBe(friends):
    real_friends = []
    for friend in friends:
        if len(friend) == 4:
            real_friends.append(friend)
    return real_friends

friends = ["Ryan", "Kieran", "Jason", "Yous"]

# MAIN

print(friends)
print(shouldBe(friends))
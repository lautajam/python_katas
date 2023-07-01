"""Timmy & Sarah think they are in love, but around where 
they live, they will only know once they pick a flower 
each. If one of the flowers has an even number of petals 
and the other has an odd number of petals it means they 
are in love.

Write a function that will take the number of petals of each 
flower and return true if they are in love and false if they aren't."""

# Return true if the flower petals are diferent (odd or even) in both cases
def love_or_lovent(he, she):
    if he % 2 == 0 and she % 2 != 0 or she % 2 == 0 and he % 2 != 0: return True
    else: return False

# MAIN

print(love_or_lovent(2,2))
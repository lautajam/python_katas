"""You were camping with your friends far away from home, but when it is 
time to go back, you realize that your fuel is running out and the nearest 
pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is 
possible to get to the pump or not.

Function should return true if it is possible and false if not."""

# Calculate if you arrive at the pump with fuel left over
def is_possible(milles_to_go, milles_per_gallon, gallons_left):
    milles_travel = milles_per_gallon * gallons_left
    if milles_travel <= milles_to_go:
        return True
    else:
        return False
    
print(is_possible(50, 25, 2))
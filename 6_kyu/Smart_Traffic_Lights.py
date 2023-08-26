"""
Story
Your friend Bob is working as a taxi driver. After working for a
month he is frustrated in the city's traffic lights. He asks you 
to write a program for a new type of traffic light. It is made so 
it turns green for the road with the most congestion.

Task
Given 2 pairs of values each representing a road (the number of 
cars on it and its name), construct an object whose turngreen method 
returns the name of the road with the most traffic at the moment of 
the method call, and clears that road from cars.

After both roads are clear of traffic, or if the number of cars on 
both roads is the same from the beginning, return an empty value instead.
"""


class SmartTrafficLight():

    """
    Args:
        street_1 (list): [number of cars, street name]
        street_2 (list): [number of cars, street name]

    Returns:
        string: street name with the most cars

    method 'turngreen()':
        returns the street name with the most cars and clears
        that street of cars. If both streets have the same number of cars
        or both streets are empty, returns None
    """

    def __init__(self, street_1, street_2):
        self.street_1 = street_1
        self.street_2 = street_2
    
    def turngreen(self):
        if self.street_1[0] == self.street_2[0]:
            return None
        elif self.street_1[0] > self.street_2[0]:
            self.street_1[0] = 0
            return self.street_1[1]
        elif self.street_1[0] < self.street_2[0]:
            self.street_2[0] = 0
            return self.street_2[1]
        else:
            print("There was a problem")

# MAIN TEST

t = SmartTrafficLight([42, "27th ave"], [72, "3rd st"])
print(t.turngreen())  # ==  "3rd st"
print(t.turngreen())  # ==  "27th ave"
print(t.turngreen())  # ==  none

r = SmartTrafficLight([10, "27th ave"], [10, "3rd st"])
print(r.turngreen())  # ==  none
"""In this kata, you should calculate type of triangle with three given sides 
a, b and c (given in any order).

If all angles are less than 90°, this triangle is acute and function should return 1.

If one angle is strictly 90°, this triangle is right and function should return 2.

If one angle more than 90°, this triangle is obtuse and function should return 3.

If three sides cannot form triangle, or one angle is 180° (which turns 
triangle into segment) - function should return 0.

Input parameters are sides of given triangle. All input values are non-negative 
floating point or integer numbers (or both).
"""

import math as m

# Applies the cosine theorem to calculate the angle of the selected side
def cosine_theorem(cathetus_selected, c2, c3):

    angle = m.asin(
        (m.pow(c2,2) + m.pow(c3,2) - m.pow(cathetus_selected, 2)) 
                            / (2 * c2 * c3)
    )

    return m.degrees(angle)

# Checks the pitagoras theorem to rigth triangles
def pitagoras_theorem(c1,c2,c3):

    h1 = m.sqrt(m.pow(c2, 2) + m.pow(c3, 2))
    h2 = m.sqrt(m.pow(c1, 2) + m.pow(c3, 2))
    h3 = m.sqrt(m.pow(c1, 2) + m.pow(c2, 2))

    if h1 == c1 or h2 == c2 or h3 == c3: return True
    else: return False

# Checks the angles of the triangle and return the type of triangle that it is
def triangle_type(c1, c2, c3):

    # # Check the pitagoras theorem
    if pitagoras_theorem(c1,c2,c3) == True: return 2

    # Calculate all angles
    angle_c1 = round(cosine_theorem(c1, c2, c3))
    angle_c2 = round(cosine_theorem(c2, c1, c3))
    angle_c3 = round(cosine_theorem(c3, c2, c1))

    # If three sides cannot form triangle  return 0
    if angle_c1 >= 180 or angle_c2 >= 180 or angle_c3 >= 180: return 0
    # If all angles are less than 90°, this triangle is acute and return 1.
    elif angle_c1 < 90 and angle_c2 < 90 and angle_c3 < 90: return 1
    # If one angle is strictly 90°, this triangle is right and return 2
    elif angle_c1 == 90 or angle_c2 == 90 or angle_c3 == 90: return 2
    # If one angle more than 90°, this triangle is obtuse and return 3.
    else: return 3

# MAIN

sides = [3,4,5]

triangle = triangle_type(sides[0], sides[1], sides[2])

if triangle == 1:
    print("The triangle is acute")
elif triangle == 2:
    print("The triangle is rigth")
elif triangle == 3:
    print("The triangle is obtuse")
else:
    print("This isn't a triangle")
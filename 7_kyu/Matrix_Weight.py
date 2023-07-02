"""A matrix is "fat" when the sum of the roots of its "Widths" is 
greater than the sum of the roots of its "Heights". Otherwise, 
we call it as a "thin" matrix.

But what is the meaning of that?

A Width of a matrix is the sum of all the elements in a row.
Similarly, a Height of a matrix is the sum of all the elements in a column.
Difficult to assimilate? Let's look at an example.

The matrix [ [1, 3] , [5, 7] ] :
  - Sum of rooted Widths: √(1+3) + √(5+7) = √4 + √12
  - Sum of rooted Heights: √(1+5) + √(3+7) = √6 + √10
  
Since "width" is smaller than "height", we determine this matrix is "thin".

The matrix [ [1, 4, 7], [2, 5, 8], [3, 6, 9] ] :
  - Sum of rooted Widths:√(1+4+7) + √(2+5+8) + √(3+6+9)  = √12 + √15 + √18  = 11.57972565...
  - Sum of rooted Heights: √(1+2+3) + √(4+5+6) + √(7+8+9) = √6 + √15 + √24 = 11.22145257...
  
Since "height" is smaller than "width", we determine this matrix is "fat".
TASK: Your task is to return "thin", "fat" or "perfect" depending on the results obtained.

NOTES:
All matrices will be squared
In case that both sums are equal, the matrix will be considered as "perfect".
DON'T round the roots... every digit matters ;)
Since the results of the roots may have a slight variation, to 
determine that a matrix is "perfect", I suggest you use an 
approximate error of 1E- 10.
If a Width or a Height is negative, return None"""

import math as m

# Takes a matrix and return her denomination
def matrix_Weight(matrix):

    sum_rooted_widths, sum_rooted_heights = 0, 0
    rooted_widths, rooted_heights = 0, 0
    margen_error = 1e-100

    # Add the roots of the rows
    for widths in matrix:
        for num in widths:
            sum_rooted_widths += num
        rooted_widths += m.sqrt(sum_rooted_widths)
        sum_rooted_widths = 0

    # Add element by element in same position, calculate the roots and add the roots
    for number_row in range(0, len(matrix)):
        for nunmber_element in range(0, len(matrix)):
            sum_rooted_heights += matrix[number_row][nunmber_element]
        rooted_heights += m.sqrt(sum_rooted_heights)
        sum_rooted_heights = 0

    if abs(sum_rooted_widths - sum_rooted_heights) < margen_error: return "The matrix is perfect."
    elif sum_rooted_widths > sum_rooted_heights: return "The matrix is 'fat'."
    else: return "The matrix is 'thin'."

# MAIN 

matrix = [ [1, 3] , [5, 7] ]

print(matrix_Weight(matrix))
    
    
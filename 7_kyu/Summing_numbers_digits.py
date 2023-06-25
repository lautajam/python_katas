"""Write a function named sumDigits which takes a number 
as input and returns the sum of the absolute value of 
each of the number's decimal digits.

For example: (Input --> Output)

10 --> 1
99 --> 18
-32 --> 5
Let's assume that all numbers in the input will be integer values."""

number = int(input("Type a integer number, please:"))

# Makes a summing digits transformming the negatives to positives and summing digits
def summing_digit_numbers(number):
    summation = 0
    # Transfor negatives numbers to positives
    if number < 0:
        number *= -1
    # Summing the digits
    for digit in str(number):
        summation += int(digit)
    return summation

print(summing_digit_numbers(number))
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# returns the average of list numbers: sum_num / len_list
def calculates_average(num_list):
    if bool(num_list) == False: return 0
    numbers = 0
    for num in num_list:
        numbers += num
    numbers = numbers/len(num_list)
    return numbers

# MAIN

num_list = [1,2,3,4,5,6,7,8,9,10]

print(calculates_average(num_list))
"""A zero-indexed array arr consisting of n integers is given. The dominator of array 
arr is the value that occurs in more than half of the elements of arr.
For example, consider array arr such that arr = [3,4,3,2,3,1,3,3]
The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is 
more than a half of 8.
Write a function dominator(arr) that, given a zero-indexed array arr consisting of n 
integers, returns the dominator of arr. The function should return -1 if array does 
not have a dominator. All values in arr will be >=0."""

numbers = [3,4,3,2,3,1,3,3]

# Search for the dominator number by checking the number of times it appears
def dominator_number(numbers):
    cant_list, cantidad, num_ant,dominator = [], 0, 0, 0

    # Creates a list with the number of times each number appears
    for number in numbers:
        for num in numbers:
            if num == number: cantidad +=1
        cant_list.append(cantidad)
        cantidad = 0

    # Designates the number appearing in more than half of the list as the dominating number
    for index in range(0, len(cant_list)):
        if cant_list[index] > num_ant and cant_list[index] > int(len(cant_list) / 2) :
            dominator = numbers[index]
            num_ant = cant_list[index]

    # if dominator is 0, no exist and return -1
    if dominator == 0: return -1
    else: return dominator

# MAIN

print(dominator_number(numbers))
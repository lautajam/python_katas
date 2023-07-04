"""A list S will be given. You need to generate a list T from it by following the given process:

Remove the first and last element from the list S and add them to the list T.
Reverse the list S
Repeat the process until list S gets emptied.
The above process results in the depletion of the list S. 
Your task is to generate list T without mutating the input List S.

Example
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]
return T

Note
size of S goes up to 10^6
Keep the efficiency of your code in mind.
Do not mutate the Input."""

# Does what the kata says
def back_forth_reverse(S):
    T = []

    # At each number (even and odd) it reverses the order in which they are stored in the list T
    for n in range(0, int(len(S)/2)):
        if n % 2 == 0:
            T.append(S[n])
            T.append(S[len(S) - n - 1])
        else:
            T.append(S[len(S) - n - 1])
            T.append(S[n])

    # If the length of the list is odd, it is necessary to add the central element of the list
    if len(S) % 2 != 0:
        T.append(S[int(len(S) / 2)])

    return T

# MAIN

print(back_forth_reverse(S=[1,2,3,4,5,6]))
print(back_forth_reverse(S=[3,45,65,234,75]))
print(back_forth_reverse(S=[10,435,4376,34567,34536,234,23,35,57,45,234]))
print(back_forth_reverse(S=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
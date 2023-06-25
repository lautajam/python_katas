"""Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed 
strings in groups. Taking the first letter of all of the inputs and grouping them next to each 
other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length."""

# Compare first group length with the second and validate if the length is the same in both
def length_validation(letters, letters_x):
    if len(letters_x) != len(letters):
        while len(letters_x) != len(letters):
            print("The length is different")
            letters_x = input("Types the letter group (same first group length): ")
    return letters_x

# Transform a string in list
def transform_list(letters):
    letters_list = []
    for let in letters:
        letters_list.append(let)
    return letters_list
    
# Transform string in list, after concatenates all list elements 
def make_string(letters, letters_2, letters_3):
    letter_list, letter_list_2, letter_list_3 = transform_list(letters), transform_list(letters_2),transform_list(letters_3)

    output = ""
    for index in range(0, len(letter_list)):
        output += letter_list[index] + letter_list_2[index] +  letter_list_3[index]

    return output
    
# MAIN

letters = input("Types the first letter group: ")
letters_2 = input("Types the second letter group (same first group length): ")
letters_2 = length_validation(letters, letters_2)
letters_3= input("Types the third letter group (same first and second group length): ")
letters_3 = length_validation(letters, letters_3)

output = make_string(letters, letters_2, letters_3)

print(output)
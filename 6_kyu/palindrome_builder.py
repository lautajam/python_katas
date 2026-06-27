"""
Task
Given a string, add the fewest number of characters possible from the front or back to make it a palindrome.

Example
For the input cdcab, the output should be bacdcab

Input/Output
Input is a string consisting of lowercase latin letters with length 3 <= str.length <= 10
The output is a palindrome string satisfying the task.
For s = ab either solution (aba or bab) will be accepted.
"""
CONDICION_DE_CORTE = "-"

def check_word(word):
    return True if len(word) >= 3 and len(word) <= 10 else False

def is_palindrome(word):
    return word == word[::-1]

def get_palindorme_complete(word):
    if not check_word(word):
        return "Does not satisfy 3 <= word <= 10"

    return "It is already a palindrome" if is_palindrome(word) else word[::-1] + word[1::]

#print(get_palindorme_complete("cdcab"))

#en proceso
def al_derecho(word):
    aux = ""
    for letter in word:
        aux_word = word   
        aux = letter + aux  
        if len(aux) == len(word) / 2:
            return CONDICION_DE_CORTE
        aux_word += aux   
        print("al derecho")
        print(aux_word)
        if is_palindrome(aux_word):
            print("si")
            return aux_word
    print("no")
    return CONDICION_DE_CORTE

def al_reves(word):
    aux = ""
    for letter in word[::-1]:
        aux_word = word[::-1]
        aux = letter + aux
        if len(aux) == len(word) / 2:
            return CONDICION_DE_CORTE
        aux_word = aux_word + aux 
        print("al reves")
        print(aux_word)
        print(aux_word)
        if is_palindrome(aux_word):
            print("si")
            return aux_word
    print("no")
    return CONDICION_DE_CORTE

def get_palindorme_complete_in_parts(word):
    if not check_word(word):
        return "Does not satisfy 3 <= word <= 10"

    if is_palindrome(word):
        return "It is already a palindrome" 
    
    aux_1 = al_derecho(word)
    print("------------------------------")
    aux_2 = al_reves(word) 
    print("------------------------------")
    if aux_1 == aux_2 and aux_1 != CONDICION_DE_CORTE:
        return word[::-1] + word[1::]
    elif aux_2 < aux_1:
        return aux_2
    else:
        return aux_1

print(get_palindorme_complete_in_parts("recono"))
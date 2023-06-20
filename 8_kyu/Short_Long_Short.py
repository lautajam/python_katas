# Given 2 strings, a and b, return a string of the form short+long+short, 
# with the shorter string on the outside and the longer string on the 
# inside. The strings will not be the same length, but they may 
# be empty ( zero length ).

# For example: (Input1, Input2) --> output

# ("1", "22") --> "1221"
# ("22", "1") --> "1221"

# Check the length of the ropes and place the shorter ones on the sides and the larger ones in the center
def shortlongshort(string_1,string_2):
    shlnsh_str = ""
    if len(string_1) > len(string_2):
        shlnsh_str = string_2 + string_1 + string_2
    elif len(string_1) < len(string_2):
        shlnsh_str = string_1 + string_2 + string_1
    else:
        shlnsh_str = string_1 + "_Both have the same length_" + string_2
    return shlnsh_str

# MAIN

print(shortlongshort(input("Please, write anything: "), input("Please, write other anything: ")))
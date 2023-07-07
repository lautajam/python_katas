"""DESCRIPTION:
Input:
    a string strng
    an array of strings arr

Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):
    a boolean true if all rotations of strng are included in arr
    false otherwise

Examples:
contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false

Note:
Though not correct in a mathematical sense

we will consider that there are no rotations of strng == ""
and for any array arr: contain_all_rots("", arr) --> true"""

# Checks if letters_rots contains all letter rotations
def contain_all_roots(letters, letters_rots):

    max_letters, rots, is_rot = letters * 2, [], 0

    for index in range(len(letters)):
        rots.append((max_letters)[index:((len(letters) + index) - len(max_letters))])
    is_rot = 0

    for rot in rots:
        if rot in letters_rots: is_rot += 1

    return True if (is_rot == len(letters)) else False
    
# MAIN

print(contain_all_roots("abcdc", ['jsj', 'abcdc', 'jkhuef', 'bcdca', 'cdcab', 'lojfu', 'dcabc', ' ihsag', 'cabcd']))
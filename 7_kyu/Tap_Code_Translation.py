"""Tap Code Translation:
Tap code is a way to communicate using a series of taps and pauses
for each letter. In this kata, we will use dots . for the taps and
whitespaces for the pauses.

The number of taps needed for each letter matches its coordinates
in the following polybius square (note the c/k position). Then you
"tap" the row, a pause, then the row. Each letter is separated
from others with a pause too.

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z

Input:
A lowercase string of a single word (no whitespaces or punctuation, only letters).

Output:
The encoded string as taps and pauses."""

# List with the code
code = (("a", "b", ("c", "k"), "d", "e"),
        ("f", "g", "h", "", "j"),
        ("l", "m", "n", "o", "p"),
        ("q", "r", "s", "t", "u"),
        ("v", "w", "x", "y", "z"))

# Check where each letter is and write the position in row/column with dots.
def tap_code_translation(code, word):
    translation = ""
    for letter in word:
        for row in code:
            for element in row:
                # Create the code, reading the position where the number is (one group of dots for the row and another group for the column)
                if letter == element:
                    secuence = ""
                    print(letter + " " + str(row) + " " +
                          str(code.index(row) + 1) + " " + str(row.index(letter) + 1))
                    for var in range(0, code.index(row) + 1):
                        secuence += "."
                    secuence += " "
                    for var in range(0, row.index(letter) + 1):
                        secuence += "."
                    translation += secuence + " "
                    break
                # if the letter is ("c", "k"), the function traverses the tuple and adds the letter
                elif letter in element:
                    secuence = ""
                    print(letter + " " + str(row) + " " +
                          str(code.index(row) + 1) + " " + str(row.index(element) + 1))
                    for var in range(0, code.index(row) + 1):
                        secuence += "."
                    secuence += " "
                    for var in range(0, row.index(element) + 1):
                        secuence += "."
                    translation += secuence + " "
                    break
    return translation

print(tap_code_translation(code, "ca/sa"))
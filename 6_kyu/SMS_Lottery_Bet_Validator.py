"""Story
You were asked to write a simple validator for a company that is planning to 
introduce lottery betting via text messages. The same validator will be used for 
multiple games: e.g. 5 out of 90, 7 out of 35, etc. (N out of M)
The text messages should contain exactly N unique numbers between 1 and M (both included), 
separated by a comma (,) and/or space(s). Any other character makes the bet invalid.

Your task
You receive the game type and the user's text message as input, and you need to check if the 
bet is valid or not. If it's valid, return the chosen numbers as a list, sorted in increasing order. 
If it's invalid, return None, null, nil as appropriate to your language.

Note: Leading and trailing spaces will not be tested. Tabs, newlines and other whitespaces are not 
tested either. Think of a classic Nokia 3310 user for reference :-)

Examples
validate_bet([5, 90], "1 2 3 4 5")       -->  [1, 2, 3, 4, 5]
validate_bet([5, 90], "5 , 3, 1  4,2")   -->  [1, 2, 3, 4, 5]
validate_bet([5, 90], "1, 2; 3, 4, 5")   -->  None / null / nil
validate_bet([5, 90], "1, 2, 3, 4")      -->  None / null / nil
validate_bet([5, 90], "1, 2, 3, 4, 95")  -->  None / null / nil"""

# Check if the wager has symbols not allowed
def check_lists(bet):

    # Creates the list with all elements
    bet_list = []
    for element in bet.replace(" ", ",").split(","):
        if element != "":
            bet_list.append(element)
    
    # This line transforms spaces into commas, then deletes the blanks and lists only numbers.
    bet_list_clean = [element for element in bet.replace(" ", ",").split(",") if element.isdigit()]

    # Compares the length of the list with all elements and that of the clean list
    if len(bet_list_clean) != len(bet_list): return False
    else: return bet_list_clean
    
# Check all parameters about the bet and return if the bet is valid or not
def validate_bet(bet, num_quant_tot, numbers_bet): 
    
    # Check if the wager has symbols not allowed
    if check_lists(bet) == False: return None
    else: bet_list_clean = check_lists(bet)
    
    # Creates a list with all integer elements
    bet_list = []
    for element in bet_list_clean:
        bet_list.append(int(element))
    
    # Check if the range of bet numbers are in the set range 
    in_range = True
    for num in bet_list:
        if num not in range(0, num_quant_tot + 1):
            in_range =  False
            break

    # If the numbers in the bet are within the range and the amount is right, give the ordered bet
    if len(bet_list) == numbers_bet and in_range == True:
        return sorted(bet_list)
    else:
        return None

# MAIN

numbers_bet = 6

num_quant_tot = 600

bet = "1,100,5,34,463,23"

answer = validate_bet(bet, num_quant_tot, numbers_bet)
print(answer)
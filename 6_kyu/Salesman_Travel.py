"""A traveling salesman has to visit clients. He got each client's address e.g. 
"432 Main Long Road St. Louisville OH 43071" as a list.

The basic zipcode format usually consists of two capital letters followed 
by a white space and five digits. The list of clients to visit was given as a 
string of all addresses, each separated from the others by a comma, e.g. :

'123 Main Street St. Louisville OH 43071,432 Main Long 
Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432'

To ease his travel he wants to group the list by zipcode.

Task
The function travel will take two parameters r 
(addresses' list of all clients' as a string) and zipcode and 
returns a string in the following format:

zipcode:street and town,street and town,.../house number,house number,...

The street numbers must be in the same order as the streets where they belong.

If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"

Examples
r = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. 
Louisville OH 43071,786 High Street Pollocksville NY 56432"

travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"

travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"

travel(r, "NY 5643") --> "NY 5643:/"""

# Takes a list of customers, a zipcode and returns only the customers with that zipcode.
def travel(r, zipcode):
    adress_list, name_adress, numeric_adress = [], "", ""

    # Gets a list ONLY with the addresses that have the zipcode
    for r_adress in r.split(","):
        if zipcode in r_adress:
            adress_list.append(r_adress)

    # If the list is empty, it returns empty.
    if len(adress_list) == 0: return zipcode + ":/"

    # Create a string with each of the addresses (numbers) and another one with the streets.
    for each_adress in adress_list:
        numeric_adress += each_adress.split(" ")[0] + ","
        name_adress += each_adress.replace(each_adress.split(" ")[0], "").replace(zipcode, "").strip() + ","

    # Remove the extra comma at the end
    numeric_adress, name_adress = numeric_adress[:-1], name_adress[:-1]

    return zipcode + ": " + name_adress + "/" + numeric_adress

# MAIN

r = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432"

print(travel(r, "OH 43071"))
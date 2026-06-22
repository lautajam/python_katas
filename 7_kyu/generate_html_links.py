"""
Generate HTML links
We need a HTML menu.... but writing HTML over and-over-again is boooring... Let's just generate it instead!

Task:
Write a function generateMenu() with the following inputs/output:

Inputs:

menuItems: An array of objects (with url and text properties), which represents our menu items

Output:

A string of HTML containing an anchor tag for each element of menuItems (with the appropriate href attribute and text content)

"""

FIRST_HTML_PART = """<!DOCTYPE html>
<html>
<head>
    <title>Menú Simple</title>
</head>
<body>

    <nav>
        <ul>\n"""

LAST_HTML_PART = """        </ul>
    </nav>

</body>
</html>
"""

# Generates a single <li> element containing an HTML link (<a>) using the given url and text
def item_generate(link, text):
    return f"           <li><a href=\"{link}\">{text}</a></li>\n"


# Iterates over a list of dictionaries (each containing url and text)
# and builds a string with all <li> HTML elements concatenated
def middle_part_generate(links_list):
    middle_part = ""
    for item in links_list:
        middle_part += item_generate(item["url"], item["text"])
    return middle_part


# Builds the complete HTML page by combining:
# - the initial HTML structure (header and opening <ul>)
# - the dynamically generated menu items
# - the final HTML structure (closing tags)
def html_complete_generate(links_list):
    return FIRST_HTML_PART + middle_part_generate(links_list) + LAST_HTML_PART

def main():
    menu_items = [
        {"url": "https://www.google.com", "text": "Google"},
        {"url": "https://www.youtube.com", "text": "YouTube"},
        {"url": "https://www.wikipedia.org", "text": "Wikipedia"},
        {"url": "https://github.com", "text": "GitHub"},
        {"url": "https://www.reddit.com", "text": "Reddit"}
    ]

    html_complete = html_complete_generate(menu_items)

    print(html_complete)


if __name__ == "__main__":
    main()
     

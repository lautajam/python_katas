"""
Introduction
In the United Kingdom, the driving licence is the official document which authorises its holder 
to operate various types of motor vehicle on highways and some other roads to which the public have access. 
In England, Scotland and Wales they are administered by the Driver and Vehicle Licensing Agency (DVLA) 
and in Northern Ireland by the Driver & Vehicle Agency (DVA). A driving licence is required in the UK by 
any person driving a vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective 
of ownership of the land over which the road passes, thus including many which allow the public to pass over private 
land; similar requirements apply in Northern Ireland under the Road Traffic (Northern Ireland) Order 1981. (Source Wikipedia)

Task
The UK driving number is made up from the personal details of the driver. The individual letters and digits can 
be code using the below information

Rules
1-5: The first five characters of the surname (padded with 9s if less than 5 characters)
6: The decade digit from the year of birth (e.g. for 1987 it would be 8)
7-8: The month of birth (7th character incremented by 5 if driver is female i.e. 51-62 instead of 01-12)
9-10: The date within the month of birth
11: The year digit from the year of birth (e.g. for 1987 it would be 7)
12-13: The initial letter of the first name and middle name, padded with a 9 if no middle name
14: Arbitrary digit - usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9
15-16: Two computer check digits. We will always use "AA"
Your task is to code a UK driving license number using an Array of data. The Array will look like

data = ["John","James","Smith","01-Jan-2000","M"]
Smith01010JJ9AA

Where the elements are as follows

0 = Forename
1 = Middle Name (if any)
2 = Surname
3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
4 = M-Male or F-Female
You will need to output the full 16 digit driving license number, in all UPPERCASE.
"""

EXTRA_PAD = "9"
FEMININE = "F"
FEMALE_MONTH_OFFSET = 50
ARBITRARY_DIGIT = "9"
CHECK_DIGITS = "AA"

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

data = ["John","James","Smith","01-Jan-2000","M"]

# Split date string into [day, month, year]
def split_date(date):
    return date.split("-")


# Format surname to 5 characters
def format_surname(apellido):
    while len(apellido) < 5:
        apellido += EXTRA_PAD
    return apellido


# Get decade and year digit from birth year
def extract_year_digits(year):
    return year[2], year[3]


# Convert month + apply gender rule
def format_month(month, gender):
    value = MONTHS[month]
    if gender == FEMININE:
        value += FEMALE_MONTH_OFFSET
    return str(value).zfill(2)


# Get initials (first name + middle name or 9)
def get_initials(names):
    return f"{names[0][0]}{names[1][0]}" if names[1] != "" else f"{names[0][0]}{EXTRA_PAD}"


# Build full driving licence
def generate_driving_license(data, year_data, date_array):
    return (
        f"{format_surname(data[2])}"
        f"{year_data[0]}"
        f"{format_month(date_array[1], data[4])}"
        f"{date_array[0]}"
        f"{year_data[1]}"
        f"{get_initials([data[0], data[1]])}"
        f"{ARBITRARY_DIGIT}"
        f"{CHECK_DIGITS}"
    ).upper()


print(
    generate_driving_license(
        data,
        extract_year_digits(split_date(data[3])[2]),
        split_date(data[3])
    )
)
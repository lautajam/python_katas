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
Where the elements are as follows

0 = Forename
1 = Middle Name (if any)
2 = Surname
3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
4 = M-Male or F-Female
You will need to output the full 16 digit driving license number, in all UPPERCASE.
"""

EXTRA_APELIDO = "9"
LIMITE_APELLIDO = 5
MASCULINO = "M"
FEMENIMO = "F"
EXTRA_FEMENINO = 50

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

data = ["John","James","Smith","01-Jan-2000","M"]

def completar_apellido (apellido):
    if len(apellido) < 5:
        while len(apellido) < 5:
            apellido += EXTRA_APELIDO
    return apellido
#print(completar_apellido("pepe"))

def decada_anio(date):
    return date.split("-")[2][2]
#print(decada_anio("3-4-2001"))

def obtain_month(date, gender):
    month = date.split("-")[1]
    number = 0
    for month_list in MONTHS.keys():
        if month == month_list:
            number = MONTHS[month_list]
    return number if gender == MASCULINO else number + EXTRA_FEMENINO
#print(obtain_month("01-Apr-2000","F"))

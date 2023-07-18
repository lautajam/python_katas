"""Create a method sayHello/say_hello/SayHello that takes as input a name, 
city, and state to welcome a person. Note that name will be an array 
consisting of one or more values that should be joined together with 
one space between each, and the length of the name array in test cases will vary.

Example:

say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!"""

def say_hello(name, city, state):
    complete_name = ""
    for name_surname in name:
        complete_name += name_surname + " "
    return "Hello, " +  complete_name[:-1] + "! Welcome to " + city + ", " + state + "!"

# MAIN

print(say_hello(['Lucía', 'González'], 'Mar del plata', 'Buenos Aires'))
print(say_hello(['Matías', 'Pérez'], 'Córdoba capital', 'Córdoba'))
print(say_hello(['Ana', 'Gutiérrez'], 'Mendoza', 'Mendoza'))
print(say_hello(['Diego', 'Fernández'], 'Rosario', 'Santa Fe'))
print(say_hello(['Carla', 'Rodríguez'], 'Mar del Plata', 'Buenos Aires'))
print(say_hello(['Federico', 'López'], 'Salta', 'Salta'))
print(say_hello(['Valentina', 'Martínez'], 'San Miguel de Tucumán', 'Tucumán'))
print(say_hello(['Sofía', 'Gómez'], 'La Plata', 'Buenos Aires'))
print(say_hello(['Juan', 'Díaz'], 'Corrientes', 'Corrientes'))
print(say_hello(['Mariano', 'Sánchez'], 'Santa Fe', 'Santa Fe'))
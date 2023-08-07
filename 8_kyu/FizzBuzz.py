
numbers = list(range(0, 101))

for number in numbers:
    if (number % 3) == 0:
        numbers[number] = "Fizz"
    if (number % 5) == 0:
        numbers[number] = "Buzz"
    if (number % 15) == 0:
        numbers[number] = "FizzBuzz"

print(numbers)
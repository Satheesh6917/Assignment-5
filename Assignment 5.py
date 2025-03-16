# list of dictionaries each representing a person with name and 'age' keys, using lambda function
people = [
    {"name": "Sai", "age": 25},
    {"name": "Bharath", "age": 17},
    {"name": "Ruthvik", "age": 19},
    {"name": "Manish", "age": 16},
    {"name": "Jaswanth", "age": 22}
]

# Filtering the people under 18
adults = filter(lambda person: person["age"] >= 18, people)

# Map the names of the remaining people to a new list
adult_names = list(map(lambda person: person["name"], adults))

print(adult_names)


#list of numbers, use the reduce function and a lambda expression to calculate the product of all the numbers

from functools import reduce

numbers = [2, 3, 4, 5]

# Use reduce to calculate the product
product = reduce(lambda x, y: x * y, numbers)
print(product)


# List of comprehension which creates a new list of squares of even numbers from a given list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension with a lambda function to check even numbers
squares_of_evens = [x**2 for x in numbers if (lambda x: x % 2 == 0)(x)]

print(squares_of_evens)


#program to check a given string is a number

is_number = lambda s: s.isdigit()

print(is_number("123"))
print(is_number("abc"))
print(is_number("12.3"))
print(is_number("-123"))


#Date time Object
from datetime import datetime
date_obj = datetime(1997, 12, 23)
# Lambda functions to extract year, month, and day
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day

# Extracting values
year = get_year(date_obj)
month = get_month(date_obj)
day = get_day(date_obj)

print(f"Year: {year}, Month: {month}, Day: {day}")


# Fibonacci Series

from functools import reduce

# Lambda function to generate Fibonacci series
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1]) if n > 1 else [0] if n == 1 else []

# Example: Generate Fibonacci series up to 10 terms
n = 10
print(fibonacci_series(n))

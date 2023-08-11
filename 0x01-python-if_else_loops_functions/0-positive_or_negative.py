#!/usr/bin/python3
import random
number = random.randint(-10, 10)
def check_number(number):
    if number > 0:
        return f"{number} is positive"
    elif number == 0:
        return f"{number} is zero"
    elif number < 0:
        return f"{number} is negative"

result = check_number(number)
print(result)

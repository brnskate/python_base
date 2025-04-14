#!/usr/bin/env python3

#numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1, 11)

for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        break
    print(f"mais codigo com {number}")

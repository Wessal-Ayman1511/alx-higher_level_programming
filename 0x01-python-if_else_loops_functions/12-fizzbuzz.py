#!/usr/bin/python3
for c in range(1, 101):
    if (c % 15 == 0):
        print('FizzBuzz', end=" ")
    elif (c % 3 == 0):
        print('Fizz', end=" ")
    elif (c % 5 == 0):
        print('Buzz', end=" ")
    else:
        print('{:d}'.format(c), end=" ")

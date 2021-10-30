## User inputs two numbers. One number is assigned to a variable, the other is assigned to another variable.
## The task is to invert the variables so that the first variable contains the second number,
## While the first number is in the second variable

# a = int(input('input value a:'))
# b = int(input('input value b:'))
#
# print(f'First a = {a}, b = {b}')
#
# a = a + b
# b = a - b
# a = a - b
#
# print(f'After swap a = {a}, b = {b}')q

## When a user enters a number, the factorial is displayed





## Our code generates a random 3-digit number and has to sum up its digits
#
# from random import randint
# random_num = randint(100, 999)
# print(f'The random number is: {random_num}')
#
# result = 0
# while random_num != 0:
#     result = result + (random_num % 10)
#     random_num = random_num // 10
#
# print (f'sum of  digits is: {result}')

##Leap year ##Leap year ##Leap year ##Leap year ##Leap year ##Leap year
#
# year = int(input('Input a year: '))
#
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print(f'{year} is a leap year')
#         else:
#             print(f'{year} is not a leap year')
#
#     else:
#         print (f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')


## Fibonacci sequence ## Fibonacci sequence ## Fibonacci sequence

def fibonacci(n):
    if n < 0:
        return 'Not a valid number'
    if n == 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    index = 3
    fib_1 = 1
    fib_2 = 1
    result = [fib_1, fib_2]

    while index <= n:
        result.append(fib_1 + fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1

    return result


print(fibonacci(9))
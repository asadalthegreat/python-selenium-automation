# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

a = int(input('input number: '))

x = 0
for num in range(a):
    x += a
    a -= 1

print('The sum of all digits from 1 to your number is ', x)



# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.
a = 0
b = 0
c = 0
li = [a, b, c]

li[0] = int(input('input first number: '))
li[1] = int(input('input second number: '))
li[2] = int(input('input third number: '))

print(li)

if li[0] > li[1]:
    if li[0] > li[2]:
        print('the bigger number is ', li[0])
elif li[1] > li[0]:
    if li[1] > li[2]:
        print('the bigger number is ', li[1])
elif li[2] > li[0]:
    if li[2] > li[1]:
        print('the bigger number is ', li[2])
else:
    print('there is no bigger number')


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0)
# and 2 odd digits (3 and 5).


x = int(input('input number: '))
print(x)
firstDigit = print(x%1000)
secondDigit = print(x%100)
thirdDigit = print(x%10)
length = len(str(x))
print('the number of digits in x is', length)



# No idea how to do this one, sorry.


# Even First
# Your input is an array of integers, and you have to reorder its entries so that
# the even entries appear first. You must solve it without allocating additional storage
# (operate with the input array)
# ex: input [7,3,5,6,4,10,3,2] output [6,4,10,2,7,3,5,3]

def even_first(arr):
    print(arr)
    write_index = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            arr.append(arr[write_index])
            arr[write_index] = arr[i]
            arr.pop(i)
            write_index = write_index + 1
    print(arr)


arr = [1,2,3]
arr = [7,3,5,6,4,10,3,2]
even_first(arr)


# Increment Number
# Write a program that takes an array of digits encoding a nonnegative decimal
# integer D and updates the array to represent the integer D + 1
# Ex: input: [1,2,9] output [1,3,0]

def increment(arr):
    list = []
    num = arr[0]*100 + arr[1]*10 + arr[2]+ 1
    list.append(int(num/100))
    list.append(int(num%100/10))
    list.append(int(num%10))

    return list


test = [1,2,9]
print(increment(test))
test = [7,8,0]
print(increment(test))
test = [4,0,7]
print(increment(test))

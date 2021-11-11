# #################### BUILT IN FUNCTIONS ####################
#
# my_list = [1, 6, 23, 7, 2, 10, 2]
# my_second_list = [976, 10]
#
# # Adding Lists Together
# print(my_list + my_second_list)
#
# # List has indices 0 ... n (size of the list - 1)
# print(my_list[2])
#
# # Negative list indices
# print(my_list[-2])
#
# # append() Adds an element at the end of the list
# print(my_list)
# my_list.append(9)
# print(my_list)
#
# # clear() removes all the elements from the list
# # my_list.clear()
# # print(my_list)
#
# # count() Returns the number of elements with the specified value
# print(my_list.count(9))
#
# # index() Returns the index of the first element with the specified value
# print(my_list.index(6))
#
# # insert() Adds an element at the specified location
# my_list.insert(1, 999)
# print(my_list)
#
# # pop() removes the element at the specified location
# my_list.pop(1)
# print(my_list)
#
#
# # remove() Removes the first item with the specified value
# my_list.remove(9)
# print(my_list)
#
# # reverse() Reverses the order of the list
# my_list.reverse()
# print(my_list)
#
# # sort() sorts the list
# my_list.sort()
# print(my_list)
#


############ CODING CHALLENGES ##############

# Input:
# [1,2,3,4,5,6,7], [3,7,2,1,4,6]
# Output:
# 5 is the missing number
#
# Step 1. sort arrays
# Step 2 Compare 2 arrays index by index
#
#

# 0(Nlog*N)
# def find_missing_num(list1, list2):
#     list1.sort()
#     list2.sort()
#
#     for num1, num2 in zip(list1, list2):
#         if num1 != num2:
#             return num1
#
#
# list1 = [1,2,3,4,5,6,7]
# list2 = [3,7,2,1,4,6]
# print(find_missing_num(list1, list2))

#### SOLUTION 2

# 0(n)
# import collections
# def find_missing_num(list1, list2):
#     dlist = collections.defaultdict(int)
#
#     for num in list2:
#         dlist[num] += 1
#
#     for num in list1:
#         if dlist[num] == 0:
#             return num
#         else:
#             dlist[num] -= 1
#
# list1 = [1,2,3,4,5,6,7]
# list2 = [3,7,2,1,6,4]
# print(find_missing_num(list1, list2))


# # Largest continuous sum
# # Given an array of integers (positive and negative) find the largest continuous sum
# # Input [1,2,-1,3,4,10,10,-10,-1]
# # Output 29(1+2+-1+3+4+10+10 = 29)
#
# def find_sum(arr):
#     if len(arr) == 0:
#         return 0
#
#     if len(arr) == 1 and arr[0] > 0:
#         return arr[0]
#
#     max_sum = current_sum = arr[0]
#
#     for num in arr[1:]:
#         current_sum = max(current_sum + num, num)
#         max_sum = max(current_sum, max_sum)
#
#     return max_sum
#
#
#
# # test_list = [-6]
# test_list = [1,2,-1,3,4,10,10,-10,-1]
# print(find_sum(test_list))

# Mountain Array
# Given an array of integers, return true if the following conditions are fulfulled:
# - length of the array is bigger than or equal to 3
#  - there exists some index i such that:
# a[0] < a[1] < .... < a[i]
# a[i] > a[i+1] > .... > a[a.size-1]
#
# basically find if there is an increasing subarray followed by a decreasing subarray
# [3,5,5] -> false
# [3,4,5,2] -> true
#
# def is_mountain(arr):
#     i = 1
#
#     while i < len(arr) and arr[i] > arr[i-1]:
#         i += 1
#
#     if i == 1 or i == len(arr):
#         return False
#
#     while i < len(arr) and arr[i] < arr[i - 1]:
#         i += 1
#
#     return i == len(arr)
#
# test_arr_neg = [3,5,5]
# test_arr_pos = [3,4,5,2]
#
# print(is_mountain(test_arr_pos)) # true
# print(is_mountain(test_arr_neg)) # false

# Move zeros
# given an array of integers, write a function to move all 0's to the end
# while maintaining the relative order of the other elements
# 0 4 0 3 12 -> 4 3 12 0 0

# def move_zeros(arr):
#
#     i = 0
#     for num in arr:
#         if num != 0:
#             arr[i] = num
#             i += 1
#
#     while i < len(arr):
#         arr[i] = 0
#         i += 1
#
#     return arr
#
# test = [0,4,0,3,12]
# print(move_zeros(test))


# Given an array of integers nums and an integer target.
# return two numbers from the array such that they add up to target
# You may assume that each input would have exactly on solution,
# and you may not use the same element twice
# You can return the answer in any order

def pair_sum(arr, k): # arr = [3, 7, 4, 9, 15, 3] target = 6
    if len(arr) < 2:
        return -1

    sum_set = set()

    for num in arr:
        target  = k - num # 6 - 3 = 3

        if target not in sum_set:
            sum_set.add(num)
        else:
            return [target, num]

test1 = [3, 7, 4, 9, 15, 3]
test_target = 18
print(pair_sum(test1, test_target))
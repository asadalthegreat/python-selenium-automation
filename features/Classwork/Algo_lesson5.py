#  0(n^2)
######### SELECTION SORT
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_list = [2, 7, 6, 1, 10, 5, 4, 8]
print(test_list)
print(selection_sort(test_list))

########## BUBBLE SORT
#  0(n^2)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

test = [1,4,5,8,9,10,19,2]
print(test)
print(bubble_sort(test))

############ INSERTION SORT
# 0(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr


test_list = [4,7,3,9,10,2,6,11]
print(test_list)
print(insertion_sort(test_list))


############# RECURSION
def recursion(num):
    print(num)
    if num == 0:
        return
    num = num -1
    recursion(num)


recursion(5)

############# MERGE SORT

# 0(n^logn)

# 0(log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

# 0(n)
def merge_arrays(l_arr, r_arr):
    merged_array = []
    i = j = 0
    while i < len(l_arr) or j <len(r_arr):
        if i == len(l_arr):
            merged_array.append(r_arr[j])
            j += 1
            continue
        if j == len(r_arr):
            merged_array.append(l_arr[i])
            i += 1
            continue

        if l_arr[i] <= r_arr[j]:
            merged_array.append(l_arr[i])
            i += 1
        else:
            merged_array.append(r_arr[j])
            j += 1

    return merged_array

test = [1,5,7,3,2,6,10,19]
print(test)
print(merge_sort(test))
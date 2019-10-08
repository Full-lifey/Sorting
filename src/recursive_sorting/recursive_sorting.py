# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    # For loop based on len(merged_arr)
    for i in range(elements):
        # If arrA or arrB are out of values?
        if len(arrA) == 0:
            # print('merged arr', merged_arr)
            merged_arr += arrB
        elif len(arrB) == 0:
            # print('merged arr', merged_arr)
            merged_arr += arrA
        else:
            # Compare first elements of arrA and arrB
            if arrA[0] < arrB[0]:
                # Pop the smaller out, inserting it into merged_arr
                smaller_item = arrA.pop(0)
                merged_arr.append(smaller_item)
            else:
                smaller_item = arrB.pop(0)
                merged_arr.append(smaller_item)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # Base case, once arrays have length of 1
    if len(arr) <= 1:
        return arr
    # Find middle of array
    mid = len(arr) // 2
    # Split array in middle
    left_split = arr[:mid]
    right_split = arr[mid:]
    # Feed arrays into merge function until only one remains
    left = merge_sort(left_split)
    right = merge_sort(right_split)
    # Merge arrays back together
    arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


def arr_split(arr2):
    if len(arr2) == 1:
        return arr2
    left = arr2[:len(arr2)//2]
    right = arr2[(len(arr2)//2):]
    # return [left, right]
    return arr_split(left), arr_split(right)

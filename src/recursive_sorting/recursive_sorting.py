# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    # For loop based on len(merged_arr)
    for i in range(elements):
        # If arrA or arrB are out of values?
        if len(arrA) == 0:
            merged_arr += arrB
            return merged_arr
        elif len(arrB) == 0:
            merged_arr += arrA
            return merged_arr
        else:
            # Compare first elements of arrA and arrB
            if arrA[0] <= arrB[0]:
                # Pop the smaller out, inserting it into merged_arr
                smaller_item = arrA.pop(0)
                merged_arr.append(smaller_item)
            else:
                smaller_item = arrB.pop(0)
                merged_arr.append(smaller_item)

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # Base case, once arrays have length of 1
    if len(arr) > 1:
        # Find middle of array
        mid = len(arr) // 2
        # Feed arrays into merge function until only one remains
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        print('left', left)
        print('right', right)
        # Merge arrays back together
        return merge(left, right)
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
    mid = len(arr) // 2
    left = merge_sort(arr2[:mid])
    right = merge_sort(arr2[mid:])
    # return [left, right]
    return merge(left, right)

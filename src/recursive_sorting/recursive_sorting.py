# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # For loop based on len(merged_arr)
    for i in range(len(merged_arr)):
        # If arrA or arrB are out of values?
        if len(arrA) == 0:
            merged_arr += arrB
        elif len(arrB) == 0:
            merged_arr += arrA
        else:
            # Compare first elements of arrA and arrB
            if arrA[0] < arrB[0]:
                # Pop the smaller out, inserting it into merged_arr
                smaller_item = arrA.pop(0)
            else:
                smaller_item = arrB.pop(0)
        merged_arr[i] = smaller_item
    # Do it again until arrA or arrB is empty
        # Merge the first item of the remaining array
        # Do it again until both arrays are empty
    return merged_arr


merge([1, 4, 7], [2, 3, 8])


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

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

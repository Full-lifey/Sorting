# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Need another loop to find smallest item in arr
        # Add first item to smallest index
        # Check if new index is smaller, if true, add to smallest_index variable
        for j in range(cur_index, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # pop smallest_index
        # insert popped item into arr[cur_index]
        popped_item = arr.pop(smallest_index)
        arr.insert(cur_index, popped_item)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

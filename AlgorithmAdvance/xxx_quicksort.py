# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    prev = low - 1  # point to the previous index of the element that need to be swap by arr[i] when we iterate.
    pivot_loc = high  # use the element in index high as pivot.
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] > pivot:
            continue
        else:  # arr[i]>=pivot
            prev = prev + 1
            arr[i], arr[prev] = arr[prev], arr[i]

    arr[prev + 1], arr[pivot_loc] = arr[pivot_loc], arr[prev + 1]

    return prev + 1


def partition_other(arr, low, high):
    prev = low #指向的比Pivot大的前一个Index，随时等着被换。或者理解为，这个Index表示包括这个Index和之前的都被换好了（已经是小于Pivot的了）。
    pivot_loc = low
    pivot = arr[low]
    for i in range(low+1, high+1):
        if arr[i] > pivot:
            continue
        else:
            prev = prev+1
            arr[i], arr[prev] = arr[prev], arr[i]
    arr[prev], arr[pivot_loc] = arr[pivot_loc], arr[prev]

    return prev

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        idx = partition_other(arr, low, high)
        quickSort(arr, low, idx - 1)
        quickSort(arr, idx + 1, high)


# Driver code to test above
arr = [3, 10, 7, 8, 9, 1, 5, 2, 4, 6]
n = len(arr)
quickSort(arr, 0, n - 1)

arr

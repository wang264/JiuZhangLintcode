def merge_sort(arr):
    merge_sort_helper(arr,left=0, right=len(arr) - 1)


def merge_sort_helper(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort_helper(arr, left, mid)
    merge_sort_helper(arr, mid + 1, right)
    merge(arr, left, mid, mid + 1, right)


def merge(array, left_start, left_end, right_start, right_end):
    n = right_end - left_start + 1
    rslt = [0] * n
    i, j = left_start, right_start
    for k in range(n):
        if i <= left_end and j <= right_end:
            # both array have values
            if array[i] <= array[j]:
                rslt[k] = array[i]
                i += 1
            else:
                rslt[k] = array[j]
                j += 1
        else:
            if i > left_end:
                rslt[k] = array[j]
            else:
                rslt[k] = array[i]

    array[left_start:right_end + 1] = rslt


array = [6, 4, 5, 7, 2, 4, 3, 4, 7, 8]

merge_sort(arr=array)

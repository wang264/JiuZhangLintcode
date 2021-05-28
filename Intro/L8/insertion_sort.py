

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        new_value = arr[i]
        j = i
        while j > 0 and arr[j - 1] > new_value:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = new_value


arr = [7, -5, 2, 16, 4]

insertion_sort(arr)





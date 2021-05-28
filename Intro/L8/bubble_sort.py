def bubble_sort(arr):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        j += 1
        for i in range(0, len(arr) - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


arr = [5, 1, 12, -5, 16]

bubble_sort(arr)

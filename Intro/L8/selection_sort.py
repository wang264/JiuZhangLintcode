# selection sort

# Selection Sort
# Selection sort is one of the O(n2) sorting algorithms, which makes it quite inefficient for sorting large data
# volumes. Selection sort is notable for its programming simplicity and it can over perform other sorts in certain
# situations (see complexity analysis for more details).

# Algorithm
# The idea of algorithm is quite simple. Array is imaginary divided into two parts - sorted one and unsorted one.
# At the beginning, sorted part is empty, while unsorted one contains whole array. At every step, algorithm finds
# minimal element in the unsorted part and adds it to the end of the sorted one. When unsorted part becomes empty,
# algorithm stops.

# When algorithm sorts an array, it swaps first element of unsorted part with minimal element and then it is included
# to the sorted part. This implementation of selection sort in not stable. In case of linked list is sorted, and,
# instead of swaps, minimal element is linked to the unsorted part, selection sort is stable.


def selection_sort(arr: list):
    n = len(arr)
    if n == 0:
        return

    for i in range(0, n):
        min_index = i
        # 在没Sort好的区间里找最小的数的Index
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # 然后换一下。 这样 index 0 --> index i 就是Sort好的了。
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [5, 1, 12, -5, 16, 2, 12, 14]
selection_sort(arr)

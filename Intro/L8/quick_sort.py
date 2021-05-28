def quickSort(A, start, end):
    if start >= end:
        return

    pivot = A[(start + end) // 2]
    left, right = start, end
    # key point 2: every time you compare left & right, it should be
    # left <= right not left < right
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1

    if left <= right:
        A[left], A[right] = A[right], A[left]
        left += 1
        right -= 1

    quickSort(A, start, right)
    quickSort(A, left, end)

def partition(A, start, end):
    # use the last element as the pivot
    pivot = A[end]

    prev = start - 1
    # prev 指向的是最后一个已经完成的不能动的部分的Index.
    for curr in range(start, end):
        # 用curr去向后找小于等于pivot的数
        if A[curr] > pivot:
            continue
        else:
            prev += 1
            A[prev], A[curr] = A[curr], A[prev]

    prev = prev + 1
    A[end], A[prev] = A[prev], A[end]
    return prev

def quickSort_2(A, start, end):
    if start >= end:
        return
    idx = partition(A, start, end)
    quickSort_2(A, start, idx - 1)
    quickSort_2(A, idx + 1, end)


A = [10, 4, 1, 2, 5, 8, -3, 3]
#A = [3, 2, 1, 4, 5]
quickSort_2(A, 0, len(A) - 1)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prefix_sum = [None] * (len(A) + 1)

prefix_sum[0] = 0

for i in range(1, len(prefix_sum)):
    prefix_sum[i] = A[i-1] + prefix_sum[i - 1]


i = 0
j = 9
prefix_sum[j+1]-prefix_sum[i]


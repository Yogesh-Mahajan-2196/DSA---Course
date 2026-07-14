arr = [1,3,4,6,9,8,5,2]
pre_sum = [0] * len(arr)
pre_sum[0] = arr[0]

for i in range(1, len(arr)):
    pre_sum[i] = pre_sum[i-1] + arr[i]

print(pre_sum)
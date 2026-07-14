arr = [1,3,4,6,9,8,5,2]
n = len(arr)
suf_sum = [0]*n

suf_sum[n-1] = arr[n-1]

for i in range(n-2, -1, -1):
    suf_sum[i] = suf_sum[i+1] + arr[i]

print(suf_sum)
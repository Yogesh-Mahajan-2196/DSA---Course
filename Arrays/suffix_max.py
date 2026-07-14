arr = [1,3,4,6,9,8,5,2]
n = len(arr)
suf_max = [0]*n
suf_max[n-1] = arr[n-1]

for i in range(n-2, -1, -1):
    suf_max[i] = max(suf_max[i+1], arr[i])

print(suf_max)
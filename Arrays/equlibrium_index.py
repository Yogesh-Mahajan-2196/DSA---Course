arr = [1,3,5,2,2]
n = len(arr)
pref_sum = [0]*n
pref_sum[0] = arr[0]

for i in range(1,n):
    pref_sum[i] = pref_sum[i-1]+arr[i]

suff_sum = [0]*n
suff_sum[n-1] = arr[n-1]

for j in range(n-2,-1,-1):
    suff_sum[j] = suff_sum[j+1] + arr[j]

for i in range(n):
    left = 0
    right = 0

    if i>0:
        left = pref_sum[i-1]
    else:
        left = 0

    if i < n-1:
        right = suff_sum[i+1]
    else:
        right = 0

    if left == right:
        print(i)
        break
else:
    print(-1)


arr_sum = sum(arr)
i = 0
j = 0

while i < n:
    if arr_sum - arr[i] == j:
        print(i)

    j += arr[i]
    arr_sum -= arr[i]
    i += 1


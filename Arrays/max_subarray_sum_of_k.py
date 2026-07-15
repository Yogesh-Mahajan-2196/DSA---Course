arr = [9,1,3,5,6,7,12,4,8]
k = 4

n = len(arr)
arr_sum = 0

for i in range(k):
    arr_sum += arr[i]

max_sum = arr_sum

for j in range(1, n-k+1):
    arr_sum = arr_sum - arr[j-1] + arr[j+k-1]
    max_sum = max(max_sum, arr_sum)

print(max_sum)
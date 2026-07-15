arr = [16,17,4,3,5,2]
n = len(arr)
suf_max = [0]*n
suf_max[n-1] = arr[n-1]

for i in range(n-2, -1, -1):
    suf_max[i] = max(suf_max[i+1], arr[i])

print(suf_max)

arr = [16,17,4,3,5,2]
n = len(arr)
leader_arr = [0]*n
leader_arr[n-1] = arr[n-1]

for i in range(n-2, -1, -1):
    leader_arr[i] = max(leader_arr[i+1], arr[i])

print(leader_arr)
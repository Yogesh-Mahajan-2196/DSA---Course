arr = [1,3,4,6,9,8,5,2]
n = len(arr)
prf_max = [0]*n

prf_max[0] = arr[0]

for i in range(1, n):
    prf_max[i] = max(prf_max[i-1], arr[i])

print(prf_max)
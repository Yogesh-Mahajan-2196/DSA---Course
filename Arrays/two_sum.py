arr = [15,23,31,18,29,16]
target = 33

arr.sort()

n = len(arr)
i = 0
j = n-1

while i<j:
    if arr[i] + arr[j] < target:
        i += 1
    elif arr[i] + arr[j] > target:
        j -= 1
    elif  arr[i] + arr[j] == target:
        print(i, j)
        break

arr = [16,17,4,3,5,2]
n = len(arr)
leader_arr = [0]*n
leader_arr[n-1] = arr[n-1]

for i in range(n-2, -1, -1):
    leader_arr[i] = max(leader_arr[i+1], arr[i])

leaders = [leader_arr[0]]
for i in range(1,len(leader_arr)):
    if leader_arr[i] != leader_arr[i-1]:
        leaders.append(i)
        
print(leaders)
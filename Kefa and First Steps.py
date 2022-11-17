n = int(input())
arr = list(map(int, input().split()))
max_count= 0
count = 0
for i in range(len(arr)-1):
    if arr[i+1]>=arr[i]:
        count+=1
    else:
        max_count = max(max_count,count)
        count=0
print(max(max_count+1,count+1))


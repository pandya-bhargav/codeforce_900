n , m = input().split()
n , m = int(n) , int(m)
matchboxes = []
for i in range(m):
    arr = [int(x) for x in input().split()]
    matchboxes.append(arr)

for i in range(0,m):
    for j in range(0,m):
        if matchboxes[i][1]>= matchboxes[j][1]:
            matchboxes[i][1],matchboxes[j][1] = matchboxes[j][1],matchboxes[i][1]
            matchboxes[i][0],matchboxes[j][0] = matchboxes[j][0],matchboxes[i][0]
matches = 0
k = 0
while n>0 and k<m:
    if matchboxes[k][0] <= n:
        matches = matches+matchboxes[k][0]*matchboxes[k][1]
        n = n - matchboxes[k][0]
        k+=1
    elif matchboxes[k][0]>n:
        matches = matches+n*matchboxes[k][1]
        k+=1
        break

print(matches)




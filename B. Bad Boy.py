n = int(input())
ans = []
for i in range(n):
    n , m , i , j = input().split()
    n , m , i , j = int(n),int(m),int(i),int(j)
    if (i==1 and j == 1) or (i==n and j == m ):
        k = [1,m,n,1]
        ans.append(k)
    else:
        k = [1,1,n,m]
        ans.append(k)
for i in range(len(ans)):
    for ele in ans[i]:
        print(ele , end = " ")
    print(end="\n")
    
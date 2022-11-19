n = int(input())
ans= []
for i in range(n):
    ele = int(input())
    l = ele//2020
    for j in range(0,l+1):
        k = (ele - 2020*j)%2021
        if k == 0:
            ans.append(1)
            break
    else:
        ans.append(0)
for ele in ans :
    if ele == 1:
        print("YES" , end = "\n")
    else:
        print("NO" , end = "\n")
    
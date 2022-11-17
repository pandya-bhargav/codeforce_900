n = int(input())
ans= []
for i in range(n):
    ele = int(input())
    for i in range(2,40):
        pw = 2**i-1
        if ele%pw==0:
            k = ele/pw
            ans.append(int(k))
            break
for ele in ans:
    print(ele, end = "\n")



n = int(input())
arr = [int(x) for x in input().split()]
k = sum(i <= -1 for i in arr)       #num of ele <= -1
zero = arr.count(0)
count = 0
for ele in arr:
    count+= abs(abs(ele)-1)
if k%2 !=0 :
    if zero>0:
        print(count)
    else:
        print(count+2)
else:
    print(count)

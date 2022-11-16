import sys
sys.stdout = open('output.txt' , 'w')
sys.stdin = open('input.txt' , 'r')
n , m = input().split()
n = int(n)
m = int(m)
# count = 0
# inter_sec = n*m
# while inter_sec!=0:
#     n = n-1
#     m = m-1
#     inter_sec = n*m
#     count+=1
# if count%2 == 0:
#     print("Malvika")
# else:
#     print("Akshat")

# other

if n>m :
    count = m
else:
    count = n
if count%2 == 0:
    print("Malvika")
else:
    print("Akshat")
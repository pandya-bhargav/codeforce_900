n = int(input())
st = input()
l = len(st)
max_count = 0
max_st = ""
for i in range(l-1):
    count = 0
    for j in range(l-1):
        if st[i]+st[i+1]==st[j]+st[j+1]:
            count+=1
    max_count = max(max_count,count)
    if count>=max_count:
        max_st = st[i]+st[i+1]
print(max_st)
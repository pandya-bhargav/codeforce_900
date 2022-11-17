string = input()
max = 0
i=0
while max < 6 and i<len(string)-1:
    if string[i]==string[i+1]:
        max +=1
    else:
        max = 0
    i+=1
if max==6:
    print("YES")
else:
    print("NO")

    
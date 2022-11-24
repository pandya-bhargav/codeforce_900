n = int(input())
ans = []
for i in range(n):
    k = input()
    ones= k.count("1")
    zeros = k.count("0")
    count = min(ones,zeros)
    if count%2 == 0:
        ans.append("NET")
    else:
        ans.append("DA")
for ele in ans:
    print(ele , end = "\n")
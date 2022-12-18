n , k = input().split()
n , k = int(n) , int(k)
arr = [ int(x) for x in input().split()]
arr.sort(reverse=True)
print(arr[k-1])
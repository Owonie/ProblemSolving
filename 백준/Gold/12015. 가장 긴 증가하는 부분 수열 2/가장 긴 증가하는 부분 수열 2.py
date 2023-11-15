from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))
x = [arr[0]]

d = [1]

for i in range(1,n):
    if x[-1] < arr[i]:
        x.append(arr[i])
        d.append(d[-1]+1)
    else:
        idx = bisect_left(x,arr[i])
        x[idx] = arr[i]
print(max(d))

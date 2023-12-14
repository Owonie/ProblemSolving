n = int(input())
arr1 =  map(int,input().split())
m = int(input())
arr2 = map(int,input().split())

ans = {}

for i in arr1:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
for j in arr2:
    if j in ans:
        print(ans[j],end=' ')
    else:
        print('0', end=' ')

import sys
input= sys.stdin.readline

n,k = map(int,input().split())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
arr.sort(reverse =True)
cnt = 0
for j in arr:
    if k / j != 0:
        cnt += k //j
        k = k%j
    else:
        break
print(cnt)

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split()))for j in range(n)]
    arr.sort()
    cnt = 1
    end = arr[0][1]
    for k in range(1,n):
        if arr[k][1] < end:
            end = arr[k][1]
            cnt += 1
    print(cnt)

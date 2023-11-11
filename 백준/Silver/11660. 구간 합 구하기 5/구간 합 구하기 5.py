# 시간제한 1초

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = []
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    temp = list(map(int,input().split()))
    num.append(temp)
for i in range(1,n+1):
    for j in range(1,n+1):
        graph[i][j] = graph[i][j-1]+ graph[i-1][j] - graph[i-1][j-1] + num[i-1][j-1]

for case in range(m):
    ans = 0
    x1,y1,x2,y2 = map(int,input().split())
    ans = graph[x2][y2] - graph[x2][y1-1]-graph[x1-1][y2] + graph[x1-1][y1-1]
    print(ans)

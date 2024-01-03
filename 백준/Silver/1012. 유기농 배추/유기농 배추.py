# 시간제한 1초

import sys
input =  sys.stdin.readline
sys.setrecursionlimit(10000)
t = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    graph[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            dfs(nx,ny)
for  _  in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    graph = [[0]*m for h in range(n)]
    for i in range(k):
        y,x = map(int,input().split())
        graph[x][y]  = 1
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                cnt += 1
                dfs(x,y)
                
    print(cnt)

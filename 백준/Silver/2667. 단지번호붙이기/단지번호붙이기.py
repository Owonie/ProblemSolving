# 시간제한 1초

import sys
input = sys.stdin.readline

n = int(input())

graph = []
ans = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
def bfs(x,y):
    global cnt
    if graph[x][y] == '1':
        graph[x][y] = '0'
        cnt += 1
        for idx in range(4):
            nx = dx[idx]+x
            ny = dy[idx]+y
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '1':
                bfs(nx,ny)
for _ in range(n):
    graph.append(list(input().rstrip()))
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            bfs(i,j)
            if cnt !=0:
                ans.append(cnt)
                cnt = 0
if len(ans) > 0:
    ans.sort()
print(len(ans))
for k in ans:
    print(k)

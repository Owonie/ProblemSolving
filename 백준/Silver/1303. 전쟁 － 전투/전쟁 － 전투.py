# 시간 제한 2초


# 그래프 입력 후 BFS로 값을 가합산
# 총 두번, B/W에 대한 값을 조회하여 비교한다

import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j,color):
    q = deque()
    q.append((i,j))
    cnt = 1
    while q:
        y,x = q.popleft()
        for idx in range(4):
            nx = x+dx[idx]
            ny = y+dy[idx]
            if 0<= nx < n and 0<= ny < m:
                if visited[ny][nx] == 0 and graph[ny][nx] == color:
                    q.append((ny,nx))
                    visited[ny][nx] = 1
                    cnt += 1
    return cnt**2
             

n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(m)]

ans = [0,0]
visited = [[0]*n for i in range(m)]

for i  in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == "W":
            visited[i][j]  =  1
            ans[0] += bfs(i,j,"W")

visited = [[0]*n for i in range(m)]

for i  in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == "B":
            visited[i][j]  =  1
            ans[1] += bfs(i,j,"B")

print(*ans)

# 시간 제한 2초

# NxM   1 -> 벽
# (1,1) -> (n,m)  최단 경로 -> BFS
# 시작 끝칸 포함
# 한개의 벽을 부술 수 있다 -> 2중 포문 BFS / 백트레킹?

# 그래프 입력 / BFS 구축
# 2중 포문 사용 또는 백 트레킹 -> 2중 시간초과
# 가지치기를 추가해볼까?


import sys
from collections import deque
input =sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j,0))
    while q:
        x,y,b = q.popleft()
        if x == n-1 and y == m-1:
            return (visited[x][y][b])
        for idx in range(4):
            nx = x+dx[idx]
            ny = y+dy[idx]
            if 0<= nx < n and 0<= ny < m:
                if b == 0 and graph[nx][ny] == '1':
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))
                elif graph[nx][ny]== '0' and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    q.append((nx,ny,b))
    return -1

n,m = map(int,input().split())
graph = [list(map(str,input().strip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

ans = bfs(0,0)

print(ans)

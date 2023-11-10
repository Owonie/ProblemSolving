# 시간제한 2초

# 1. 그래프 / visited / dx,dy 만들기
# 2. 3중 for문 만들기
# 3. bfs구현하기
# 4. 바이러스 좌표일 때 -> q에 넣고 상하좌우

import sys
input = sys.stdin.readline
import copy
from collections import deque
from itertools import combinations

n,m = map(int,input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
graph = []
space = []
for _ in range(n):
    temp = list(map(str,input().split()))
    for i in range(m):
        if temp[i] == '0':
            space.append((_,i))
    graph.append(temp)

def bfs(walls):
    cnt = 0
    q = deque([])
    temp = copy.deepcopy(graph)
    for wall in walls:
        x,y = wall
        temp[x][y] = '1'
    for i in range(n):
        for j in range(m):
            if temp[i][j] == '2':
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == '0':
                    temp[nx][ny] = '2'
                    q.append((nx,ny))
    cnt = 0
    for i in range(n):
        cnt += temp[i].count('0')
    return cnt

ans = 0
for i in combinations(space,3):
    ans = max(ans,bfs(i))
  
print(ans)

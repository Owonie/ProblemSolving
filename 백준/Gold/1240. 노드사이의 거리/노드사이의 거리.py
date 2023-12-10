# 시간 제한 2초
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(start,end):
    q = deque()
    q.append((start,0))
    visited = [False]* (n+1)
    visited[start] = True
    while q:
        node,distance = q.popleft()
        if node == end:
            return distance
        for i,d in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i,distance+d))
        
for _ in range(m):
    a,b  = map(int,input().split())
    print(bfs(a,b))

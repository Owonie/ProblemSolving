#시간제한 2초 
from collections import deque

n,k = map(int, input().split())

def bfs(n):    
    visited = [0] * 100001
    q = deque()
    q.append(n)
    visited[n] = 1
    
    while q:
        position = q.popleft()
        if position == k:
            return visited[position]
        for idx in (position - 1,position + 1,  position * 2):
            if 0 <= idx < 100001 and visited[idx] == 0:
                if idx == position * 2:
                    visited[idx] = visited[position]
                    q.appendleft(idx)
                else:
                    visited[idx] = visited[position] + 1
                    q.append(idx)

ans = bfs(n)
print(ans-1)

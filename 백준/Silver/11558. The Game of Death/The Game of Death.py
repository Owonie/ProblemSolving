# 시간제한 1초
import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    check[node] = 1

    while queue:
        curr = queue.popleft()

        for n in graph[curr]:
            if check[n] == 0:
                check[n] = check[curr] + 1
                queue.append(n)

for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        v = int(input())
        graph[i].append(v)
    check = [0] * (N+1)
    bfs(1)
    print(check[N]-1 if check[N] > 0 else 0)

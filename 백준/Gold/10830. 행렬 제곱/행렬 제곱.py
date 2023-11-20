# 시간제한 1초

import sys
input = sys.stdin.readline
n,b = map(int,input().split())

graph = []

for _ in range(n):
    temp = list(map(int,input().split()))
    graph.append(temp)


def mul(A,B,n):
    rst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rst[i][j]+= (A[i][k] * B[k][j])
            rst[i][j] %= 1000
    return rst
# mul -> A,B 곱해준다 ( conq )

# divide가 필요

for i in range(n):
    for j in range(n):
        graph[i][j] %= 1000
rst = [[0] * n for _ in range(n)]
for i in range(n):
    rst[i][i] = 1
while b!= 0:
    if b%2 == 1:
        rst = mul(rst,graph,n)
    graph = mul(graph,graph,n)
    b >>= 1
for i in range(n):
    for j in range(n-1):
        print(rst[i][j], end=' ')
    print(rst[i][-1])

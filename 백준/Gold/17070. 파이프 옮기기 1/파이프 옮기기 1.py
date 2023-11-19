# 시간제한 1초

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())

# 파이프 라인에 따라 분류를 한다
# 가로 / 대각선 -> 우측이동
# 세로 / 대각선 -> 아래측 이동
# 가로 / 대각선 / 세로 -> 대각선 이동


HO = 0
VIR = 1
DIAG = 2
graph = []
graph = [list(map(int,input().split())) for _ in range(n)]
cnt= 0


def dfs(nowy, nowx, type):
    global cnt
    if (nowy,nowx) == (n-1,n-1):
        cnt += 1
        return

    if type == HO or type == DIAG:
        if nowx+1 < n and graph[nowy][nowx+1] == 0:
            dfs(nowy, nowx+1, HO)
    if type == VIR or type == DIAG:
        if nowy + 1 < n and graph[nowy+1][nowx] == 0:
            dfs(nowy+1, nowx, VIR)
    if nowx+1 <n and nowy+1 < n:
        if graph[nowy+1][nowx] == 0 and graph[nowy][nowx+1] == 0 and graph[nowy+1][nowx+1] == 0:
                 dfs(nowy+1, nowx+1, DIAG)
dfs(0,1,HO)
print(cnt)

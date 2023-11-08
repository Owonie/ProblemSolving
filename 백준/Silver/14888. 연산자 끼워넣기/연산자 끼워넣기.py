# 시간제한 2초

# 수는 고정 연산자 변경 가능

# 식의 계산은 연산자 우선 순위를 무시한다

# 나눗셈은 정수 나눗셈으로 몫만 취한다.

# 최대값 / 최소값 구하기 -> 완전탐색

# 시간초과가 뜬다 -> 백트레킹

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ope = list(map(int,input().split()))
min_ans = 1e9
max_ans = -1e9
def dfs(depth,plus,minus,multi,divide,ans):
    global min_ans,max_ans
    if depth == n:
        min_ans = min(ans,min_ans)
        max_ans = max(ans,max_ans)
    if plus > 0:
        dfs(depth+1,plus-1,minus,multi,divide,ans+arr[depth])
    if minus > 0:
        dfs(depth+1,plus,minus-1,multi,divide,ans-arr[depth])
    if multi > 0:
        dfs(depth+1,plus,minus,multi-1,divide,ans*arr[depth])
    if divide > 0:
        dfs(depth+1,plus,minus,multi,divide-1,int(ans/arr[depth]))
dfs(1,ope[0],ope[1],ope[2],ope[3],arr[0])
print(max_ans)
print(min_ans)

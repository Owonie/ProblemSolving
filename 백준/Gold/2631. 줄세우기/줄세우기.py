# 시간 제한 1초

# 정렬?
# 모든 경우의 수를 저장

# LIS 최장 배열

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
dp = [0 for _ in range(n)]
dp[0] = 1
temp = 0
for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j]:
            temp = max(temp,dp[j])
    dp[i] = temp+1
    temp = 0
print(n-max(dp))

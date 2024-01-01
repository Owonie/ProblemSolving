import sys
input = sys.stdin.readline

dp = [0]*301
arr = [0]*301


n = int(input())
for _ in range(n):
    arr[_] = int(input())

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[1]+arr[2], arr[0]+arr[2])

for i in range(3,n):
    dp[i] = max(arr[i]+dp[i-2],arr[i]+arr[i-1]+dp[i-3])

print(dp[n-1])

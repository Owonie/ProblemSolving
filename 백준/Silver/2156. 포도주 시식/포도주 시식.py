# 시간제한 2초

# w[i]+w[i-1]+dp[i-3] 전전 안마심
# w[i] + d[i-2] 전전 마시고  전 안마심
# d[i-1] 안마심

# 1 2 3 4 -> 1 3 4 / 1 2 4 / 1 2 3

n = int(input())
w = []
dp = [0] * n

for i in range(n):
    w.append(int(input()))

dp[0] = w[0]
if n > 1:
    dp[1] = w[0]+w[1]
if n > 2:
    dp[2] = max(w[2]+w[1],w[2]+w[0],dp[1])
for i in range(3,n):
    dp[i] = max(dp[i-1],dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i])
print(dp[n-1])

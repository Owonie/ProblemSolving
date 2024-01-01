n,k = map(int,input().split())
w = [0]
v = [0]
knapsack = [[0]* (k+1) for _ in range(n+1)]
for _ in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)
for i in range(1,n+1):
        for j in range(1,k+1):
            if w[i] > j:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j]= max(knapsack[i-1][j],knapsack[i-1][j-w[i]]+v[i])
print(knapsack[n][k])

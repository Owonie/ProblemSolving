# 시간제한 10초

n = int(input())
col = [0] * n
ans = 0
def promising(i):
    for k in range(i):
        if (col[i] == col[k] or abs(col[k]-col[i]) == abs(k-i)):
            return False
    return True

def dfs(i):
    global ans
    if i == n:
        ans += 1
        return
    else:
        for j in range(n):
            col[i] = j
            if promising(i):
                dfs(i+1)

dfs(0)
print(ans)

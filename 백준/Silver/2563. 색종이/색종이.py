# 시간제한 1초

n = int(input())
arr = [[0]*100 for _ in range(100)]
ans = 0

for _ in range(n):
    a,b = map(int,input().split())
    # 색종이 표시
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j]=1
# 면적 구하기
for _ in arr:
    ans += _.count(1)

print(ans)

# 시간제한 2초

# 첫번째 정렬 -> 시작시간이 빠른 회의

# 두번째 정렬 -> 짧은 시간인 회의

# 빨리 시작해서 제일 짧은 회의만 골라서 하면 정답
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort()
arr.sort(key=lambda x:x[1])
end = 0
cnt = 0
for _ in range(n):
    if end <= arr[_][0]:
        cnt += 1
        end = arr[_][1]
print(cnt)
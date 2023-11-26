# 시간제한 1초

# 회의실 문제
# 선 정렬 후 3가지 조건에 대해 분기처리

import sys

input = sys.stdin.readline

n = int(input())

# 튜플로 시간초과 방지
arr = list(tuple(map(int, input().split())) for _ in range(n))
arr.sort()

start = arr[0][0]
end = arr[0][1]
ans = 0

for k in range(1, n):
    now_start, now_end = arr[k]
    # 1. 겹칩
    if end > now_start:
        end = max(end, now_end)

    # 2. 안 겹침
    else:
        ans += (end - start)
        # 새로운 걸로 업데이트
        start, end = now_start, now_end

ans += (end - start)
print(ans)

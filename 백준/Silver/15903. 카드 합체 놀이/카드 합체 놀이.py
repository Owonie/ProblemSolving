# 시간제한 1초

# 정렬 -> 작은거끼리 합치기 -> 정렬 -> m번 반복
# 정렬은 그냥 heap 쓰면 된다.

import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())

arr = list(map(int,input().split()))
heapq.heapify(arr)

for i in range(m):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    heapq.heappush(arr, a+b)
    heapq.heappush(arr, a+b)
print(sum(arr))
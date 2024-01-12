# 시간 제한 1초

# 첫 숫자만 정한다면 그 뒤 순서는 상관 없다.

n = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse =True)

ans = arr[0]

for i in range(1,n):
    ans += arr[i]/2

print('%g'%ans)

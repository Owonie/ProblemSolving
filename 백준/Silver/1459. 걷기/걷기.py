# 시간제한 2초

# 사선 : min(2*w,s)
# 직선 : 짝수 -> min(w,s) 홀수-> s 한번 쉬고 min(w,s) + w
import sys
input = sys.stdin.readline
time = 0
x,y,w,s = map(int,input().split())

diag = min(2*w,s)
direct = min(w,s)
ans = 0
if abs(x-y) % 2 == 0:
    ans = min(x,y) * diag + abs(x-y) * direct
else:
    ans = min(x,y) * diag + (abs(x-y)-1) * direct + w

print(ans)
# 시간제한 1초

a,k = map(int,input().split())

cnt =  0

while True:
    if a == k:
        print(cnt)
        break
    else:
        if k % 2 == 0 and k >= 2 * a:
            k = k // 2
            cnt += 1
        else:
            k -= 1
            cnt += 1

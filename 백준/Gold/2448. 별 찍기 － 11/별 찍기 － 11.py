# 시간제한 1초


n = int(input())
arr = [[' ' for _ in range(n*2)] for _ in range(n)]

def conq(x, y, index):
    if index <= 3:
        for i in range(3):
            for j in range(i+1):
                arr[x+i][y+j] = arr[x+i][y-j] = '*'
        arr[x+1][y] = ' '
        return
    mid = index // 2
    conq(x, y, mid)
    conq(x+mid, y-mid, mid)
    conq(x+mid, y+mid, mid)
    
conq(0, n-1, n)
for i in range(n):
    print("".join(arr[i]))

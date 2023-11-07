# 시간제한 2초

import sys

N = int(sys.stdin.readline())
matrix = []
result = [0,0,0]

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# 종이의 유효성 검사
def check(x,y,n):
    value = matrix[x][y]
    for i in range(n):
        for j in range(n):
            if value != matrix[x+i][y+j]:
                return False
    return True

def divide(x,y,n):
    # 온전한 종이일 때 result에 추가 
    if check(x,y,n):
        result[matrix[x][y]+1] += 1
    # 아닐 경우 자르기 시도
    else:
        for i in range(3):
            for j in range(3):
                divide(x+i*n//3,y+j*n//3,n//3)
    return
divide(0,0,N)
for i in range(3):
    print(result[i])

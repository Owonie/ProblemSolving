import sys
input = sys.stdin.readline

def solve():
    m,n = map(int,input().split())
    arr = {}
    for _ in range(m):
        word = input().rstrip()
        if len(word) < n:
            continue
        if word not in arr:
            arr[word] = 1
            continue
        arr[word] += 1
    arr = sorted(arr.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))
    for i in arr:
        print(i[0])
solve()

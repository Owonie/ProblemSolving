n = int(input())

arr = []
ans = []

for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in range(n):
    ans.append(arr[i]*(i+1))
print(max(ans))
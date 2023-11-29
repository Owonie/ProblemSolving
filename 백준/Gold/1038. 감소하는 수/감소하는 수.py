# 시간제한 1초

n = int(input())

arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def dp() :
    if n < 10:
        return arr[n]

    idx = 1
    while len(arr) < n + 1:
        if len(arr) <= idx:
            return -1
        for s in range(0, int(arr[idx][-1])):
            desc = arr[idx] + arr[s]
            arr.append(arr[idx] + arr[s])
            if len(arr) == n + 1:
                return arr[-1]
        idx += 1

    return arr[-1]


print(dp())

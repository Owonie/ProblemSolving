def solution(s):
    arr = ['A']
    for i in s:
        if arr[-1] == i:
            arr.pop()   
        else:
            arr.append(i)
    if arr == ['A']:
        return 1
    return 0

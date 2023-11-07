def solution(numbers,target):
    arr = [0]
    for i in numbers:
        arr2 = []
        for j in arr:
            arr2.append(j-i)
            arr2.append(j+i)
        arr = arr2
    return arr.count(target)
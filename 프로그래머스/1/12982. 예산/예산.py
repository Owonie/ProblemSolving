def solution(d, budget):
    answer = 0
    count = 0
    d.sort()
    print(d)
    for i in d:
        answer += i
        if answer > budget:
            return count
        count+= 1
    return count 

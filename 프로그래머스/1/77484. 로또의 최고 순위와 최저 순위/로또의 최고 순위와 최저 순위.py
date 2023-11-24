def solution(lottos, win_nums):
    cnt = 0
    answer = [0,0]
    zero = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    if cnt == 6:
        return [1,1]
    if cnt == 0 and zero == 0:
        return [6,6]
    if zero == 6:
        return [1,6]
    answer[0] = 6-cnt-zero+1
    answer[1] = 6-cnt+1
    return answer

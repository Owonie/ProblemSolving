def solution(s):
    answer =[]
    cnt = 0
    tb = 0

    while True:
        if s  == '1':
            break
        tb += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        cnt += 1
    answer = [cnt,tb]
    return answer

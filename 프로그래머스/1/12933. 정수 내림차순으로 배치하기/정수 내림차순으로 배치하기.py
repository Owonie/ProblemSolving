def solution(n):
    answer = ''
    s = list(map(int,str(n)))
    s.sort(reverse = True)
    answer = ''.join(map(str,s))
    return int(answer)

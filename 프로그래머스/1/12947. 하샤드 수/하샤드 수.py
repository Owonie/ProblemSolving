def solution(n):
    s = list(map(int,str(n)))
    if n % sum(s) == 0:
        return True
    return False


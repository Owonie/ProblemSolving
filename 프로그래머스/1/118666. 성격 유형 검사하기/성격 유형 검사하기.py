def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        a = survey[i][0]
        b = survey[i][1]
        if choices[i] > 4 :
            dic[b] += choices[i] -4
        elif choices[i] < 4:
            dic[a] += 4 - choices[i]
    answer += "R" if dic["R"] >= dic["T"] else "T"
    answer += "C" if dic["C"] >= dic["F"] else "F"
    answer += "J" if dic["J"] >= dic["M"] else "M"
    answer += "A" if dic["A"] >= dic["N"] else "N"
    return answer
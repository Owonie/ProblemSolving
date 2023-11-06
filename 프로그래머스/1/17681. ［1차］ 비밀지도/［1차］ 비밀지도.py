def solution(n, arr1, arr2):
    answer = []
    result= ''
    a1=[]
    a2=[]
    for i in range(n):
        a1.append(bin(arr1[i])[2:].zfill(n))
        a2.append(bin(arr2[i])[2:].zfill(n))
    for i in range(n):
        for j in range(n):
            if a1[i][j] == '1' or a2[i][j] == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
        result = ''
    return answer

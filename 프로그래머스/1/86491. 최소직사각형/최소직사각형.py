def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    for s in sizes:
        w = s[0]
        h = s[1]
        width.append(w)
        height.append(h)
    answer = max(width) * max(height)
    return answer
        

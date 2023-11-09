def solution(rows, columns, queries):
    graph = [[0]*columns for _ in range(rows)]
    cnt = 1
    answer = []
    
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt +=1
    for _ in queries:
        arr = []
        prev_graph = [item[:] for item in graph]
        for i in range(_[0],_[2]+1):
            for j in range(_[1],_[3]+1):
                if j == _[1] and i != _[2]:
                    graph[i-1][j-1] = prev_graph[i][j-1]
                    continue
                if j == _[3] and i != _[0]:
                    graph[i-1][j-1] = prev_graph[i-2][j-1]
                    continue
                if i == _[0]:
                    graph[i-1][j-1] = prev_graph[i-1][j-2]
                    continue
                if i == _[2]:
                    graph[i-1][j-1] = prev_graph[i-1][j]

        for i in range(rows):
            for j in range(columns):
                if graph[i][j] != prev_graph[i][j]:
                    arr.append(graph[i][j])
        answer.append(min(arr))

    return answer

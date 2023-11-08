def solution(n, computers):
    answer = 0
    visited = [False] * n
    print(visited)
    for i in range(n):
        if visited[i] == False:
            dfs(n , computers, visited, i)
            answer += 1
    return answer

def dfs(n, computers, visited, i):
    visited[i] = True

    for j in range(n):
        if computers[i][j] == 1 and i != j:
            if visited[j] == False:
                dfs(n, computers, visited,j)
    

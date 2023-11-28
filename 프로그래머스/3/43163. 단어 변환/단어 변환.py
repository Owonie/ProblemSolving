from collections import deque

def solution(begin, target, words):
    q = deque()
    lenght = len(words)
    word_length = len(begin)
    def check(word,change):
        temp = 0
        for i in range(word_length):
            if word[i] != change[i]:
                temp += 1
        if temp == 1:
            return True
        else:
            return False
    def bfs():
        q.append([begin,0])

        if target not in words:
            return 0
        while q:
            word, depth = q.popleft()

            for change in words:
                if check(word,change):
                    if change == target:
                        return depth + 1

                    else:
                        q.append([change,depth+1])
    ans = bfs()
    return ans
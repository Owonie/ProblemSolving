check = [False] * 10
max_ans = ""
min_ans = ""
k = int(input())
arr = list(map(str,input().split()))

def is_True(a,b,c):
    if c  == '<':
        return a < b
    else:
        return a > b
# 백트래킹 요소 -> 인덱스(탐색깊이) + 정수
def backtrack(idx,num):
    global max_ans,min_ans
    # promising / prunning 을 정해주자
    # promising:
    if idx == k+1:
        if len(min_ans) == 0:
            min_ans = num
        else:
            max_ans = num
        return
    for i in range(10):
        if check[i] == False:
            # 처음 시작했거나, 부등호 관계를 만족할때
            if idx ==0 or is_True(num[-1],str(i),arr[idx-1]):
                check[i] = True
                backtrack(idx+1,num+str(i))
                check[i] = False
    


backtrack(0,'')
print(max_ans)
print(min_ans)

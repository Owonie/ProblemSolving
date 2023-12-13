# 시간 제한 1초
# m 과 n 의 문제와 거의 똑같다.
# promising 부분만 수정하자.

n,m = map(int,input().split())

ans = []
# 인덱스를 넣어준다.
def backtrack(idx):
    if len(ans) == m:
        print(*ans)
        return
    # 시작점을 이전에 넣은 숫자 뒤에부터 시작한다.
    for i in range(idx,n+1):
        if i not in ans:
            ans.append(i)
            backtrack(i+1)
            ans.pop()
# 첫 인덱스는 1         
backtrack(1)
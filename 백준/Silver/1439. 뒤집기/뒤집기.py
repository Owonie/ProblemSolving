# 시간제한 2초

s = input()

s_one = s.split('0')
s_zero = s.split('1')

ans = [0] * 2
for i in s_one:
    if i != '':
        ans[0] += 1

for j in s_zero:
    if j != '':
        ans[1] += 1

print(min(ans))

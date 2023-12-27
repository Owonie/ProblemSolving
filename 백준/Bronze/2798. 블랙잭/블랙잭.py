from itertools import combinations

n, s = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0

for c in combinations(cards, 3):
    if sum(c) <= s and sum(c) > max_sum:
        max_sum = sum(c)
print(max_sum)
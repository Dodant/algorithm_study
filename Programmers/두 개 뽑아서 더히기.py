from itertools import combinations

def solution(l):
    answer = set()
    for a, b in list(combinations(l, 2)):
        answer.add(a+b)
    return sorted(list(answer))

print(solution([2,1,3,4,1]))
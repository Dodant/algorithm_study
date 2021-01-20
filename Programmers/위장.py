from itertools import combinations
from functools import reduce

def solution(clothes):
    result = len(clothes)
    clothe_dict = dict()
    for item in clothes:
        if item[1] not in clothe_dict: clothe_dict[item[1]] = 1
        else: clothe_dict[item[1]] += 1

    data = clothe_dict.values()
    if len(clothe_dict) == len(clothes): return 2 ** len(clothes) - 1
    if len(clothe_dict) == 1: return result

    for i in range(2, len(clothe_dict)+1):
        prep = list(combinations(data, i))
        for j in prep:
            result += reduce(lambda a, b: a*b, j)
    return result


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
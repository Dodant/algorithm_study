def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


def solution_me(answers):
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    mul = len(answers)
    su1_answer = (su1*mul)[:mul]
    su2_answer = (su2*mul)[:mul]
    su3_answer = (su3*mul)[:mul]

    count1, count2, count3 = 0, 0, 0

    for i in range(len(su1_answer)):
        if answers[i] == su1_answer[i]: count1 += 1

    for i in range(len(su2_answer)):
        if answers[i] == su2_answer[i]: count2 += 1

    for i in range(len(su3_answer)):
        if answers[i] == su3_answer[i]: count3 += 1

    max_num = max(count1, count2, count3)

    result = []
    if max_num == count1: result.append(1)
    if max_num == count2: result.append(2)
    if max_num == count3: result.append(3)
    return result
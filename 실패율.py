def solution(N, stages):
    answer = []
    rate = []
    for i in range(1, N+1):
        not_clear_count = len([ply for ply in stages if ply == i])
        clear_count = len([ply for ply in stages if ply >= i])
        if clear_count == 0:
            rate.append((i, 0))
        else:
            rate.append((i, not_clear_count/clear_count))

    for i in sorted(rate, key=lambda x: -x[1]):
        answer.append(i[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(6, [1, 1, 2, 2, 2]))
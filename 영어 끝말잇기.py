def solution(n, words):
    error_point = 1000
    duple_point = 1000
    last = words[0][-1]
    for i in range(1, len(words)):
        if words[i][0] == last:
            last = words[i][-1]
        else:
            error_point = i
            break
    # print(error_point)
    if len(set(words)) != len(words):
        word_dict = dict()
        for idx, item in enumerate(words):
            if item not in word_dict:
                word_dict[words[idx]] = 1
            else:
                duple_point = idx
                break
    # print(duple_point)
    if error_point == 1000 and duple_point == 1000:
        return [0, 0]

    error_point = min(error_point, duple_point)
    return [error_point%n+1, error_point//n+1]

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
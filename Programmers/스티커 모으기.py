def solution(sticker):
    if len(sticker) in (0,1,2):
        return max(sticker)

    # 첫번쨰 스티커를 뜯지 않는 경우
    d = [0] * len(sticker)
    d[0] = 0
    d[1] = sticker[1]

    for i in range(2, len(sticker)):
        d[i] = max(d[i-1], d[i-2] + sticker[i])
    answer_one = max(d)

    # 첫번쨰 스티커를 뜯은 경우
    d = [0] * len(sticker)
    d[0] = sticker[0]
    d[1] = d[0]

    for i in range(2, len(sticker)-1):
        d[i] = max(d[i-1], d[i-2] + sticker[i])
    answer_two = max(d)

    return max(answer_one, answer_two)

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
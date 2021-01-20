def solution(dartResult):
    # answer = list(dartResult)
    result = []
    idx = 0

    while idx < len(dartResult):
        # 10 걸러내기
        if dartResult[idx] == '1' and dartResult[idx+1] == '0':
            result.append(10)
            idx += 2
            continue
        elif dartResult[idx].isdigit():
            result.append(int(dartResult[idx]))
            idx += 1
            continue

        if dartResult[idx].isalpha():
            if dartResult[idx] == "S":
                result[-1] = result[-1] ** 1
            elif dartResult[idx] == "D":
                result[-1] = result[-1] ** 2
            elif dartResult[idx] == "T":
                result[-1] = result[-1] ** 3
            idx += 1
            continue
        else:
            if len(result) >= 2 and dartResult[idx] == "*":
                result[-2] *= 2
                result[-1] *= 2
                idx += 1
            elif dartResult[idx] == "*":
                result[-1] *= 2
                idx += 1
            elif dartResult[idx] == "#":
                result[-1] = -result[-1]
                idx += 1

    return sum(result)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

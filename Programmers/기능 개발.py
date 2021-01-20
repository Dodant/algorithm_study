def solution(progresses, speeds):
    result = []
    time, count = 0, 0
    while progresses:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                result.append(count)
                count = 0
            time += 1
    result.append(count)
    return result

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([96, 99, 98, 97], [1, 1, 1, 1]))
print(solution([93, 30, 55, 60], [1, 30, 5, 40]))
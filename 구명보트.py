def solution(people, limit):
    people.sort(reverse=True)
    boat = len(people)
    s, e = 0, len(people) - 1
    while s < e:
        if people[s] + people[e] <= limit:
            boat -= 1
            e -= 1
        s += 1
    return boat


print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 50, 80], 100)) # 3
print(solution([160, 150, 140, 60, 50, 40], 200)) #3
print(solution([20, 50, 50, 80], 100))
print(solution([40, 40, 40], 100))
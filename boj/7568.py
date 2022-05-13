import sys 
sys.stdin = open('data.txt', 'r')

people = []

for _ in range(int(input())):
    people.append(tuple(map(int, input().split())))

rank = []

for i in range(len(people)):
    cnt = 1
    for j in range(len(people)):
        if i == j:
            pass
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    rank.append(cnt)

print(*rank)
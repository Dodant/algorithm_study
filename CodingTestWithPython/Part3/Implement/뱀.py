n = int(input())
arr = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

l = int(input())
direction = []
for _ in range(l):
    t, d = input().split()
    direction.append((int(t), d))

body = [(0, 0)]
snake = body[0]

# 상 우 하 좌
dire = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
x, y = body[0]
while True:
    # 방향 전환
    if len(direction) != 0:
        if direction[0][0] == count:
            if direction[0][1] == "D":
                dire += 1
                if dire == 4:
                    dire = 0
            elif direction[0][1] == "L":
                dire -= 1
                if dire == -1:
                    dire = 3
            direction.pop(0)

    # 범위 밖으로 나갔을 때
    if x+dx[dire] >= n or x+dx[dire] <= -1 or y+dy[dire] >= n or y+dy[dire] <= -1:
        print(count+1)
        break

    # 사과를 먹는 경우
    if arr[x+dx[dire]][y+dy[dire]] == 1:
        body.append((x+dx[dire], y+dy[dire]))
        x += dx[dire]
        y += dy[dire]
        count += 1
    # 사과를 먹지 않는 경우
    else:
        if (x+dx[dire], y+dy[dire]) in body:
            print(count+1)
            break
        body.pop(0)
        body.append((x+dx[dire], y+dy[dire]))
        x += dx[dire]
        y += dy[dire]
        count += 1

    print(body)
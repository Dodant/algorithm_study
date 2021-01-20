n, m = map(int, input().split())
ball_list = list(map(int, input().split()))

count = 0

for i in range(len(ball_list)):
    for j in range(i, len(ball_list)):
        if ball_list[i] != ball_list[j]:
            count += 1

print(count)

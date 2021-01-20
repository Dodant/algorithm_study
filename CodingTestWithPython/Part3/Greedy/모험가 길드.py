n = int(input())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

count = 0
while num_list:
    for i in range(num_list[0]):
        num_list.pop(0)
    count += 1

print(count)
from collections import deque

list_ = deque()
for i in range(int(input())):
    input_num = int(input())
    if input_num == 0:
        list_.pop()
        continue
    list_.append(input_num)
print(sum(list_))

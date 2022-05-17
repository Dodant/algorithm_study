n, k = map(int, input().split())

from collections import deque
stack = deque([i for i in range(1, n+1)])
yosepus = []

while stack:
    for i in range(k-1):
        stack.append(stack.popleft())
    yosepus.append(stack.popleft())

print('<', ', '.join(map(str, yosepus)), '>', sep='')

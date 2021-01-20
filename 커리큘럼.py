from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
time = [0] * (v+1)
graph = [[] for _ in range(v+1)]
graph2 = [[] for _ in range(v+1)]

for i in range(1, v+1):
    cost, *pack, _ = map(int, input().split())
    time[i] = cost
    for j in pack:
        indegree[i] += 1
        graph[j].append(i)
        graph2[i].append(j)

print(time)
print(indegree)
print(graph)
print(graph2)


def topology_sort():
    result = []
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        max_time = 0
        mark = 0
        for j in graph2[i]:
            if max_time < time[j]:
                max_time = time[j]
                mark = j
        time[i] += time[mark]

topology_sort()
print()
print(time)
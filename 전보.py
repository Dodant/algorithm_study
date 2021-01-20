import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        if dist + i[1] < distance[i[0]]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(q, (dist + i[1], i[0]))


print(len([i for i in distance if i <= INF])-2, max([i for i in distance if i < INF]))
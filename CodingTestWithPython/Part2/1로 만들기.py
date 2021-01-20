[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
[0,1,1,2,1,2,3,3,2, 2, 3, 3, 4, 4, 2]

n = int(input())

d = [0]*100
d[1] = 0
d[2] = 1
d[3] = 1
d[5] = 1

def makeone(n):
    if d[n] != 0:
        return d[n]
    for i in range(2, n+1):
        time = [100, 100, 100, 100]
        if i % 5 == 0:
            time[0] = d[i // 5]
        if i % 3 == 0:
            time[1] = d[i // 3]
        if i % 2 == 0:
            time[2] = d[i // 2]
        if d[i - 1] != 0:
            time[3] = d[i - 1]
        d[i] = min(time) + 1
    return d[n]


print(makeone(n))
print(d)
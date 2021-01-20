# n까지 채우는 방법

# a(n) = 2*a(n-2) + a(n-1)
# a(1) = 1
# a(2) = 3
# a(3) = 5
# a(4) = 11

n = int(input())
d = [0]*1001
d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3,n+1):
    d[i] = (d[i-2]*2 + d[i-1]) % 796796

print(d[n])
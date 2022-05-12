import sys 
sys.stdin = open('data.txt', 'r')

bag = []

for _ in range(int(input())):
    bag.append(int(input()))

bag.sort()
print('\n'.join(map(str, bag)))


### fast ver
import sys
n = int(input())
l = []

for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
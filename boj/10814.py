import sys
sys.stdin = open('data.txt', 'r')

people = []
for i in range(int(input())):
    age, name = input().split()
    people.append(tuple(int(age), name))

people.sort()
print(people)

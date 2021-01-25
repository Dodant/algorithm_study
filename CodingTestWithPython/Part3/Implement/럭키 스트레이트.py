n = list(input())

first, last = n[:len(n)//2], n[len(n)//2:]

if sum(list(map(int, first))) == sum(list(map(int, last))):
    print("Lucky")
else:
    print("Ready")
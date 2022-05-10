import sys 
sys.stdin = open('data.txt', 'r')

n = int(input())
word_bag = []

for i in range(n):
    text = str(input())
    word_bag.append(text)

word_bag = list(set(word_bag))
word_bag.sort()
word_bag.sort(key=len)
print('\n'.join(word_bag))
import sys 
sys.stdin = open('data.txt', 'r')

n, m = map(int, input().split())
board = [str(input()) for _ in range(n)]

b_first = 'BWBWBWBW'
w_first = 'WBWBWBWB'

b_chess = (b_first + w_first) * 4
w_chess = (w_first + b_first) * 4

least_color = 10000

def box_extract(board, i, j):
    box = ''
    for a in range(8):
        for b in range(8):
            box += board[i+a][j+b]
    return box

def compare(chess, box):
    count = 0
    for i in range(len(chess)):
        if box[i] != chess[i]: count += 1
    return count

for i in range(n-7):
    for j in range(m-7):
        box = box_extract(board, i, j)
        a = compare(b_chess, box)
        b = compare(w_chess, box)
        color = min(a, b)
        if color < least_color:
            least_color = color

print(least_color)


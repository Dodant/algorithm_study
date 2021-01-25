n = list(input())

char_list = []
num_l = 0

for i in n:
    if i.isalpha():
        char_list.append(i)
    else:
        num_l += int(i)

char_list.sort()
print("".join(char_list), num_l, sep="")
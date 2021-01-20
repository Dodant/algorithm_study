num_str = input()
answer = int(num_str[0])

for i in num_str[1:]:
    if i == '1' or answer == 1:
        answer += int(i)
        continue
    if i == '0':
        continue
    answer *= int(i)

print(answer)
bin_str = input()
bin_str += bin_str[-1]

zeros_count = 0
ones_count = 0

for i in range(0, len(bin_str)-1):
    if bin_str[i] == '1' and bin_str[i+1] == '0':
        zeros_count += 1
    elif bin_str[i] == '0' and bin_str[i + 1] == '1':
        ones_count += 1

print(max(zeros_count, ones_count))
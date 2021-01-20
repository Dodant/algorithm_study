def solution(s):
    s = s.lower()
    lst1 = list(s.split())
    lst2 = list(s)
    answer = []
    for i in lst1:
        wrd = []
        for j in range(len(i)):
            if j % 2 == 0: wrd.append(i[j].upper())
            else: wrd.append(i[j])

        answer.append("".join(wrd)) # [TrY, HeLlO, WoRlD]

    buffer_list = []
    buffer = ""
    for i in range(len(lst2)):

        if not lst2[i].isalpha():
            buffer += lst2[i]
            if i == len(lst2) - 1:
                buffer_list.append(buffer)
        elif lst2[i].isalpha() and len(buffer) != 0:
            buffer_list.append(buffer)
            buffer = ""

    result = ""
    if lst2[0].isalpha():
        while buffer_list and answer:
            result += answer.pop(0)
            result += buffer_list.pop(0)
        if not lst2[-1].isalpha():
            while buffer_list:
                result += buffer_list.pop(0)
    else:
        while buffer_list and answer:
            result += buffer_list.pop(0)
            result += answer.pop(0)

    while answer:
        result += answer.pop(0)

    return result

print(solution("try  hello   world      eeee   "))
print(solution("  try  hello world  eeee"))
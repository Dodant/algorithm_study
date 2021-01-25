def solution(s):
    min_answer = len(s)

    for step in range(1, len(s)//2+1):
        count = 1
        example = ""
        for i in range(0, len(s), step):
            if s[i:i+step] == s[i+step:i+step+step]:
                count += 1
            else:
                if count == 1:
                    example += s[i:i+step]
                    count = 1
                    continue
                example += str(count) + s[i:i+step]
                count = 1
        if len(example) < min_answer:
            min_answer = len(example)
    return min_answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))

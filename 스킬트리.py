def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        result = ''
        for alpha in skill_tree:
            if alpha in skill:
               result += alpha
        if result == skill[:len(result)]:
            count += 1
    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
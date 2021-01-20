import copy

def solution(garden):
    update_garden = copy.deepcopy(garden)
    sqr = len(garden)*len(garden[0])
    count = 0
    while update_garden != [[1]*len(garden[0]) for i in range(len(garden))]:
        for i in range(len(garden)):
            for j in range(len(garden[0])):
                if garden[i][j] == 1:
                    if i+1 != len(garden):
                        update_garden[i+1][j] = 1
                    if j+1 != len(garden[0]):
                        update_garden[i][j+1] = 1
                    if i-1 != -1:
                        update_garden[i-1][j] = 1
                    if j-1 != -1:
                        update_garden[i][j-1] = 1
        count += 1
        garden = copy.deepcopy(update_garden)

    return count

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
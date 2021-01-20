def solution(K, words):
    num_list = list(map(lambda a: len(a), words))
    count = 0
    store = 0
    for i in num_list:
        if (store + i) < K and store != 0:
            store += 1 + i
        else:
            store = i
            count += 1
    return count



# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"] # 4,5,5,5,2
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
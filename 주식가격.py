def solution(prices):
    result = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                count+=1
                break
            count+=1
        result.append(count)
    return result

print(solution([1,2,3,2,3]))
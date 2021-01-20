import heapq

def solution(food_times, k):
    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    heapq.heapify(food_times)

    small_food = food_times[0][0]
    prev_food = 0

    while k - ((small_food - prev_food) * len(food_times)) >= 0:
        k -= (small_food - prev_food) * len(food_times)
        prev_food, _ = heapq.heappop(food_times)
        if not food_times:
            return -1
        small_food = food_times[0][0]

    food_times = sorted(food_times, key=lambda x: x[1])
    return food_times[k % len(food_times)][1]

    # while k > 0:
    #     while food_times[pointer] == 0:
    #         pointer += 1
    #         if pointer == len(food_times):
    #             pointer = 0
    #
    #     food_times[pointer] -= 1
    #     k -= 1
    #     pointer += 1
    #     if pointer == len(food_times):
    #         pointer = 0
    #     if k == 0:
    #         while food_times[pointer] == 0:
    #             pointer += 1
    #             if pointer == len(food_times):
    #                 pointer = 0
    #
    # return pointer + 1



print(solution([3, 1, 2], 5))           # answer = 1
print(solution([4,2,3,6,7,1,5,8], 16))  # answer = 3
print(solution([4,2,3,6,7,1,5,8], 27))  # answer = 5
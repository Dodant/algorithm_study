list_ = list(map(int, input().split()))

while list_ != list(range(1, 6)):
    if list_[0] > list_[1]:
        list_[0], list_[1] = list_[1], list_[0]
        print(*list_)
    if list_[1] > list_[2]:
        list_[1], list_[2] = list_[2], list_[1]
        print(*list_)
    if list_[2] > list_[3]:
        list_[2], list_[3] = list_[3], list_[2]
        print(*list_)
    if list_[3] > list_[4]:
        list_[3], list_[4] = list_[4], list_[3]
        print(*list_)
    

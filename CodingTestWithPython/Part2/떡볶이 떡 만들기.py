n, quan = map(int, input().split())
dduk = list(map(int, input().split()))
new_list = [0 for _ in range(max(dduk)+1)]

def right_dduk(quan, dduk, start, end):
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        sumdduck = 0
        for i in dduk:
            if mid < i:
                sumdduck += i - mid
        if sumdduck == quan:
            return mid
        elif sumdduck > quan:
            start = mid + 1
        else:
            end = mid - 1
    return mid

print(right_dduk(quan, dduk, 0, max(dduk)))
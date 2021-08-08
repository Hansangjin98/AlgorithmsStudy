N = int(input())
targetArray = sorted(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    find = False
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if targetArray[mid] == i:
            find = True
            print(1)
            break
        elif targetArray[mid] < i:
            start = mid + 1
        elif targetArray[mid] > i:
            end = mid - 1
    if not find:
        print(0)
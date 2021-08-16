N, M = map(int, input().split())
arr = list(map(int, input().split()))
right = sum(arr)
left = max(arr)

while left <= right:
    mid = (left + right) // 2
    cnt, sum_lesson = 1, 0

    for i in range(len(arr)):
        if arr[i] > mid:
            break
        elif sum_lesson + arr[i] <= mid:
            sum_lesson += arr[i]
        else:
            cnt += 1
            sum_lesson = arr[i]
    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1

print(left)
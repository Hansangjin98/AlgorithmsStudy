N = int(input())
arr = []
result = 0
for _ in range(N):
    arr.append(list(input()))

def check(arr):
    maxCount = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                count += 1
            else:
                count = 1
            if count > maxCount:
                maxCount = count

        count = 1
        for j in range(1, N):
            if arr[j][i] == arr[j-1][i]:
                count += 1
            else:
                count = 1
            if count > maxCount:
                maxCount = count
    return maxCount

for i in range(N):
    for j in range(N):
        if j+1 < N:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = check(arr)
            if temp > result:
                result = temp
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if j+1 < N:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            temp = check(arr)
            if temp > result:
                result = temp
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
print(result)
Y, X = map(int, input().split())
arr, result = [], []

for _ in range(Y):
    arr.append(list(input()))

for s in range(Y-7):
    for e in range(X-7):
        white = 0
        black = 0
        for i in range(s, s+8):
            for j in range(e, e+8):
                if (i + j) % 2 == 0:
                    if arr[i][j] != 'W': white += 1
                    if arr[i][j] != 'B': black += 1
                else:
                    if arr[i][j] != 'B': white += 1
                    if arr[i][j] != 'W': black += 1
        result.append(white)
        result.append(black)
print(min(result))
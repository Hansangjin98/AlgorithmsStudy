N = int(input())
mul = N // 5
result = 0
cannotFlag = False

if (N % 5) % 2 == 0:
    result += mul + (N % 5) // 2
else:
    while (N - (5 * mul)) % 2 != 0:
        if mul > 0 :
            mul -= 1
        else:
            cannotFlag = True
            break
    if cannotFlag:
        result = -1
    else:
        result += mul + (N - 5*mul) // 2
print(result)
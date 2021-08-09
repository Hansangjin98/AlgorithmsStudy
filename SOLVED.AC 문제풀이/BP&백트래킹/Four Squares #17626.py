N = int(input())

if (N ** 0.5).is_integer():
    print(1)
    exit()
for i in range(1, int(N ** 0.5) + 1):
    if N < i ** 2:
        break
    if ((N - i ** 2) ** 0.5).is_integer():
        print(2)
        exit()
for i in range(1, int(N ** 0.5) + 1):
    if N < i ** 2:
        break
    for j in range(1, int(N ** 0.5) + 1):
        if N < (i ** 2) + (j ** 2):
            break
        if (((N - i ** 2) - (j ** 2)) ** 0.5).is_integer():
            print(3)
            exit()
print(4)
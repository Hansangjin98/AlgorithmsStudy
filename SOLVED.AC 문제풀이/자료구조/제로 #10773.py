K = int(input())
array = []
result = 0

for _ in range(K):
    inp = int(input())
    if inp == 0:
        del array[-1]
    else:
        array.append(inp)

for i in range(len(array)):
    result += array[i]

print(result)
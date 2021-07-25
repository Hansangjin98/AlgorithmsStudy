w = input()
f = input()
i = 0
result = 0
while i <= len(w)-len(f):
    if w[i:i + len(f)] == f:
        result += 1
        i += len(f)
    else:
        i += 1
print(result)
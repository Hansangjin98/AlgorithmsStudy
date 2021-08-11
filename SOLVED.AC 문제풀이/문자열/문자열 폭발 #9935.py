w = input()
p = input()
compare = []
for i in p:
    compare.append(i)
stack = []

for i in range(len(w)):
    stack.append(w[i])
    if stack[-len(p):] == compare:
        for _ in range(len(p)):
            stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
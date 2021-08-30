import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    C = sys.stdin.readline().split()
    if len(C) == 2:
        stack.append(C[1])
        continue
    if C[0] == 'top':
        print(stack[-1]) if len(stack) else print(-1)
    elif C[0] == 'size':
        print(len(stack))
    elif C[0] == 'empty':
        print(0) if len(stack) else print(1)
    elif C[0] == 'pop':
        print(stack.pop()) if len(stack) else print(-1)
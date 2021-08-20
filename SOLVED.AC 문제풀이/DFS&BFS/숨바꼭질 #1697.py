from collections import deque

N, K = map(int, input().split())
visited = [False] * (K*2)

def bfs(start):
    count = 0
    q = deque([[start, count]])

    while q:
        t = q.popleft()
        v = t[0]
        count = t[1]
        if not visited[v]:
            visited[v] = True
            if v == K:
                return count
            count += 1
            if (v * 2) <= (K*2):
                q.append([v*2, count])
            if (v + 1) <= (K*2):
                q.append([v+1, count])
            if (v - 1) >= 0:
                q.append([v-1, count])
    return count

print(bfs(N))
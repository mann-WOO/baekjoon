# Kurskal 시간초과

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


N, K = map(int, input().split())
edges = []
for _ in range(K):
    n1, n2, w = map(int, input().split())
    edges.append((w, n1, n2))
edges.sort()
p = [i for i in range(N)]
cnt = 1
total = 0
result_edges = []
for w, n1, n2 in edges:
    if find_set(n1) != find_set(n2):
        result_edges.append((w, n1, n2))
        cnt += 1
        total += w
        if n1 < n2:
            n1, n2 = n2, n1
        p[find_set(n1)] = find_set(n2)
        if cnt == N+1:
            break

adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
for (w, n1, n2) in result_edges:
    adj_matrix[n1][n2] = w
    adj_matrix[n2][n1] = w
cost = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    q = [i]
    visited = [0 for _ in range(N)]
    visited[i] = 1
    while q:
        current = q.pop(0)
        for j in range(N):
            if adj_matrix[current][j] and not visited[j]:
                visited[j] = 1
                cost[i][j] = cost[i][current] + adj_matrix[current][j]
                q.append(j)

max_cost = 0
for i in range(N):
    for j in range(N):
        if cost[i][j] > max_cost:
            max_cost = cost[i][j]

print(total)
print(max_cost)
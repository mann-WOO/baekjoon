# Prim 어떻게?

N, K = map(int, input().split())
adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    n1, n2, w = map(int, input().split())
    adj_matrix[n1][n2] = w
    adj_matrix[n2][n1] = w
costs = [1000000 for _ in range(N)]
mst = [0 for _ in range(N)]

costs[0] = 0
mst[0] = 1
current = 0
cnt = 1
sum_costs = 0

while cnt <= N-1:
    for i in range(N):
        if adj_matrix[current][i] and adj_matrix[current][i] < costs[i]:
            costs[i] = adj_matrix[current][i]

    for i in range(N):
        if not mst[i]:
            next = i
            break
    for i in range(next, N):
        if costs[i] < costs[next] and not mst[i]:
            next = i

    mst[next] = 1
    cnt += 1
    sum_costs += costs[next]
    current = next

print(sum_costs)

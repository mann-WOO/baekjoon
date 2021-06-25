N, M, K = map(int, input().split())
generators = list(map(int, input().split()))
connections = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    connections[u][v] = w
    connections[v][u] = w
costs = [10001 for _ in range(N+1)]
mst = [0 for _ in range(N+1)]
sum_costs = 0
for generator in generators:
    costs[generator] = 0
    mst[generator] = 1
for generator in generators:
    for i in range(1, N+1):
        if connections[generator][i] and connections[generator][i] < costs[i]:
            costs[i] = connections[generator][i]
current = generators[0]
while sum(mst) < N:
    for i in range(N+1):
        if connections[current][i] and connections[current][i] < costs[i]:
            costs[i] = connections[current][i]
    for i in range(N+1):
        if not mst[i]:
            next_node = i
            break
    for i in range(next_node, N+1):
        if costs[i] < costs[next_node] and not mst[i]:
            next_node = i
    mst[next_node] = 1
    sum_costs += costs[next_node]
    current = next_node

print(sum_costs)
# 도시의 수 N, 간선의 수 M, 발전소의 수 K
N, M, K = map(int, input().split())
# 발전소 리스트 generators
generators = list(map(int, input().split()))
# 인접행렬 connections
connections = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    connections[u][v] = w
    connections[v][u] = w
# 도시가 추가되는 비용을 기록할 costs -> 최댓값으로 초기화
costs = [10001 for _ in range(N+1)]
# mst의 추가 여부를 기록할 mst
mst = [0 for _ in range(N+1)]
# 비용의 합 sum_costs
sum_costs = 0
# 발전소는 연결비용이 0, mst에 추가되어 있음
for generator in generators:
    costs[generator] = 0
    mst[generator] = 1
# 각 발전소에서 갈 수 있는 도시의 연결 비용을 갱신
for generator in generators:
    for i in range(1, N+1):
        if connections[generator][i] and connections[generator][i] < costs[i]:
            costs[i] = connections[generator][i]
# 첫 번째 발전소에서 mst 연결 시작
current = generators[0]
# mst 에 모든 도시가 연결될 때까지
while sum(mst) < N:
    # 현재 도시에서 갈 수 있는 비용 갱신
    for i in range(N+1):
        if connections[current][i] and connections[current][i] < costs[i]:
            costs[i] = connections[current][i]
    # 도시 중 mst에 연결되어 있지 않고, 가장 적은 비용으로 연결될 수 있는 곳을 찾기
    for i in range(N+1):
        if not mst[i]:
            next_node = i
            break
    for i in range(next_node, N+1):
        if costs[i] < costs[next_node] and not mst[i]:
            next_node = i
    # mst에 연결
    mst[next_node] = 1
    # 해당 연결 비용을 비용의 합에 합산
    sum_costs += costs[next_node]
    # 다음 도시로 설정
    current = next_node

print(sum_costs)
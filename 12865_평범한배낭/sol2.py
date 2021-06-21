# 시간초과: dp를 이용한 재귀

# 물품의 수 N, 최대 무게 K
N, K = map(int, input().split())

# 물건들의 무게, 가치 리스트
weights = []
values = []
for i in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)


# 가치를 반환하는 knapsack 함수
def knapsack(capacity, n):
    global N
    # 마지막 물건까지 확인했거나, 무게한도를 다 썼을 때, value를 추가할 수 없으므로 0 반환
    if K == 0 or n == N:
        return 0
    # 현재 확인중인 물건이 남은 무게한도보다 무겁다면 넣을 수 없으므로 다음 물건 확인
    if weights[n] > capacity:
        return knapsack(capacity, n+1)
    # 넣을 수 있다면 넣는 경우와 넣지 않는 경우 중 더 높은 가치를 가지는 경우의 가치를 반환
    else:
        return max(values[n] + knapsack(capacity-weights[n], n+1), knapsack(capacity, n+1))


print(knapsack(K, 0))

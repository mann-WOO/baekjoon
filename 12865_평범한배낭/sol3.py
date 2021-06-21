# 물품의 수 N, 최대 무게 K
N, K = map(int, input().split())

# 물건들의 무게, 가치 리스트
weights = []
values = []
for i in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)


# 최대 무게와 물건의 수를 인자로 받는 knapsack 함수
def knapsack(capacity, n):
    # array[i][j]: 배낭 크기가 j일 때, i개의 물건을 넣었을 때 가능한 최대 가치
    array = [[0 for _ in range(capacity+2)] for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            # 물건의 무게가 j보다 클 때
            if weights[i-1] > j:
                array[i][j] = array[i-1][j]
            # 물건의 무게가 j보다 작거나 같을 때
            else:
                array[i][j] = max(values[i-1] + array[i-1][j-weights[i-1]], array[i-1][j])
    return array[n][capacity]


print(knapsack(K, N))

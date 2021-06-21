# 시간초과: combination의 재귀 구현

# 물품의 수 N, 최대 무게 K
N, K = map(int, input().split())

# 각 물건의 (무게 W, 가치 V) 쌍 리스트
items = []
for i in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# 가능한 가치값들의 리스트 초기화
values = []


# 조합 생성함수
def find_combination(weigh, value, n):
    global N, K
    # 마지막 물건까지 확인하면 가능한 가치값을 추가
    if n == N:
        values.append(value)
        return
    # 현재 물건 가방에 넣지 않고 다음 물건 확인
    find_combination(weigh, value, n+1)
    # 현재 물건을 가방에 넣었을 때 최대 무게를 넘지 않는다면 넣고 다음 물건 확인
    if weigh + items[n][0] <= K:
        find_combination(weigh + items[n][0], value + items[n][1], n+1)


# 첫 번째 물건부터 확인
find_combination(0, 0, 0)


# 가치값들 중 최댓값을 출력
result = max(values)
print(result)


T = int(input())

for tc in range(1, T+1):
    # 가게의 개수 num_sotre
    num_store = int(input())
    # 집의 위치 home
    home = list(map(int, input().split()))
    # 편의점들의 위치 stores
    stores = [list(map(int, input().split())) for _ in range(num_store)]
    # 목적지의 위치 end
    end = list(map(int, input().split()))
    # 편의점 방문여부 visited
    visited = [0 for _ in range(len(stores))]
    # dfs를 위한 stack 초기화
    stack = [home]
    # 결과값을 불가능으로 초기화
    result = 'sad'

    # stack을 비울 때까지 dfs
    while stack:
        # 스택에서 하나 꺼내 현재위치로 설정
        current = stack.pop()
        # 현재위치에서 목적지에 도달 가능하다면 결과값 갱신 후 종료
        if abs(current[0] - end[0]) + abs(current[1] - end[1]) <= 1000:
            result = 'happy'
            break
        # 현재위치에서 목적지에 도달할 수 없다면 현재위치에서 갈 수 있고, 아직 방문하지 않은 편의점을 스택에 추가
        for i in range(num_store):
            if not visited[i] and abs(current[0] - stores[i][0]) + abs(current[1] - stores[i][1]) <= 1000:
                stack.append(stores[i])
                visited[i] = 1

    # 결과값 출력
    print(result)

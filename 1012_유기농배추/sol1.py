T = int(input())
# 델타이동 행, 열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for tc in range(1, T+1):
    # 입력값으로 2차원 배열 fields 생성
    M, N, K = map(int, input().split())
    fields = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        fields[x][y] = 1
    # 결과값(상하좌우로 연결된 밭의 수)
    count = 0
    # fields를 순회하면서
    for i in range(N):
        for j in range(M):
            # 밭을 만나면
            if fields[i][j]:
                # 결과값에 1 합산
                count += 1
                # 상하좌우 dfs 하면서 연결된 배추밭을 0으로 만들기
                stack = [(i,j)]
                while stack:
                    cr, cc = stack.pop()
                    fields[cr][cc] = 0
                    # 상하좌우 네방향 중 진출할 수 있고 밭인 부분을 스택에 추가
                    for k in range(4):
                        nr, nc = cr+dr[k], cc+dc[k]
                        if 0 <= nr < N and 0 <= nc < M and fields[nr][nc]:
                            stack.append((nr, nc))
    print(count)
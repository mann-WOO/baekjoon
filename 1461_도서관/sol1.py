N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

# 절대값들의 합 구하기(부호 판별 위해)
abs_sum = 0
for book in books:
    abs_sum += abs(book)
# 결과값 초기화
result = 0
# 부호가 모두 같은 경우
if abs(sum(books)) == abs_sum:
    # 모두 음수
    if books[0] < 0:
        for i in range(0, N, M):
            result += 2*abs(books[i])
        # 가장 값이 큰 곳은 갔다가 돌아오지 않음
        result -= abs(books[0])
    # 모두 양수
    else:
        for i in range(N-1, -1, -M):
            result += 2*abs(books[i])
        result -= abs(books[-1])
# 부호가 다른 원소가 있는 경우
else:
    # 첫번째 양수 지점 찾기
    for i in range(len(books)):
        if books[i] > 0:
            first_positive = i
            break
    # 오른쪽 끝이 더 먼 경우: 왼쪽 다 가고, 오른쪽 끝에서 멈추기
    if abs(books[0]) <= abs(books[-1]):
        # 왼쪽 가기
        for i in range(0, first_positive, M):
            result += 2*abs(books[i])
        # 오른쪽 가기
        for i in range(N-1, first_positive-1, -M):
            result += 2 * abs(books[i])
        result -= abs(books[-1])
    # 왼쪽 끝이 더 먼 경우: 오른쪽 다 가고, 왼쪽 끝에서 멈추기
    else:
        # 오른쪽 가기
        for i in range(N-1, first_positive-1, -M):
            result += 2 * abs(books[i])
        # 왼쪽 가기
        for i in range(0, first_positive, M):
            result += 2*abs(books[i])
        result -= abs(books[0])

print(result)

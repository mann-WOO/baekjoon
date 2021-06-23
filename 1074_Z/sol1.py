N, r, c = map(int, input().split())

# 사각현 한변의 길이 length
length = 2**N

# 방문순서 result
result = 0
# 정사각형 한 변의 길이를 반씩 줄여가기
while length > 1:
    # 반으로 줄인 길이를 length로
    length = int(length/2)
    # 반으로 줄인 길이보다 아래에 있다면 위의 반을 지나오기 때문에 결과에 그 크기를 합산
    if r >= length:
        result += 2*(length**2)
        r -= length
    # 반으로 줄인 길이보다 오른쪽에 있다면 왼쪽 반의반을 지나오기 때문에 결과에 그 크기 합산
    if c >= length:
        result += length**2
        c -= length

print(result)

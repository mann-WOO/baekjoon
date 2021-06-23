minus = 0
zero = 0
plus = 0


# 하나로만 이루어져 있는지 확인하는 함수
def union_check(array, end_row, end_col, length):
    number = array[end_row-length][end_col-length]
    for i in range(end_row-length, end_row):
        for j in range(end_col-length, end_col):
            if array[i][j] != number:
                return False
    return True


# 종이를 나누는 함수(array, 행의 끝 idx+1, 열의 끝 idx+1, 사각형 한 변의 길이)
def divide(array, end_row, end_col, length):
    global minus, zero, plus
    # 하나로만 이루어져 있는지 확인
    union = union_check(array, end_row, end_col, length)
    # 하나로만 이루어져 있다면
    if union:
        number = array[end_row - length][end_col - length]
        if number == -1:
            minus += 1
        elif number == 0:
            zero += 1
        else:
            plus += 1
        return
    # 하나로 이루어져 있지 않다면 더 작은 사각형 한 변의 길이 구하기
    small_length = int(length / 3)
    # 작은 사각형 만들어 다시 divide
    for i in range(end_row-length+small_length, end_row+1, small_length):
        for j in range(end_col-length+small_length, end_col+1, small_length):
            divide(array, i, j, small_length)


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

divide(array, N, N, N)
print(f'{minus}\n{zero}\n{plus}')
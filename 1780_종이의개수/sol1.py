# 시간초과

minus = 0
zero = 0
plus = 0


# 하나로만 이루어져 있는지 확인하는 함수
def union_check(array):
    number = array[0][0]
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] != number:
                return False
    return True


# 종이를 나누는 함수
def divide(array):
    global minus, zero, plus
    # 하나로만 이루어져 있는지 확인
    union = union_check(array)
    # 하나로만 이루어져 있다면
    if union:
        if array[0][0] == -1:
            minus += 1
        elif array[0][0] == 0:
            zero += 1
        else:
            plus += 1
        return
    # 하나로 이루어져 있지 않다면 더 작은 사각형 한 변의 길이 구하기
    length = int(len(array)/3)
    # 작은 사각형 만들어 다시 divide
    for i in range(length, len(array)+1, length):
        for j in range(length, len(array)+1, length):
            small_array = []
            for k in range(i-length, i):
                small_array.append(array[k][j-length:j])
            divide(small_array)


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

divide(array)
print(f'{minus}\n{zero}\n{plus}')
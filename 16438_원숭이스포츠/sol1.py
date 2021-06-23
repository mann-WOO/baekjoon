# 반씩 나눠서 뒤 절반의 팀을 바꿔주는 것을 n번 반복하는 함수 divide
def divide(n, array):
    if n == 0:
        return array
    else:
        # 중심점 기준으로 오른쪽의 알파벳을 바꿔줌
        mid = len(array)//2
        for i in range(mid, len(array)):
            array[i] = 'B' if array[i] == 'A' else 'A'
            # 반으로 나눠 다음 분할 진행
        return divide(n-1, array[0:mid]) + divide(n-1, array[mid:len(array)])


N = int(input())

# 7번의 경기동안 반복
for i in range(1, 8):
    result = divide(i, ['A' for _ in range(N)])
    print(''.join(result))
times = [300, 60, 10]


def get_minimum(t):
    # 예외처리
    if t % 10:
        return -1
    # 조작 횟수 기록할 results
    results = [0, 0, 0]
    # 남은 시간 기록할 remain
    remain = t
    # 큰 시간부터 사용할 수 있다면 빼주기 모두 배수관계이므로
    for i in range(3):
        while remain >= times[i]:
            remain -= times[i]
            results[i] += 1
    results = list(map(str, results))
    return ' '.join(results)


T = int(input())
result = get_minimum(T)
print(result)


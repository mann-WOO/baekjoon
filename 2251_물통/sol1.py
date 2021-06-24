# 각 물통의 최대 용량 limit
limit = list(map(int, input().split()))
# 생성 가능한 경우의 수 results
results = []


# 1. 받을 물통이 비어 있다면
# 1-1. 받을 물통에 남은 공간이 줄 물통의 물 양보다 적거나 같다면 -> 가득 찰 때까지만 붓는다
# 1-2. 받을 물통에 남은 공간이 줄 물통의 물 양보다 크다면 -> 모두 붓는다
def pour(array):
    # 현재의 상태가 기록되어 있는지 확인, 기록되어 있다면 넘어가기
    if array in results:
        return
    # 기록되어 있지 않다면 기록하고 물 붓는 동작 수행
    else:
        results.append(array)
    # 모든 물통들을 확인
    for i in range(3):
        # 물통에 물이 있다면
        if array[i]:
            # 해당 물통을 제외한 물통들(targets)에 물을 줄 수 있음
            targets = [0, 1, 2]
            targets.remove(i)
            # 물을 받을 물통들을 확인
            for target in targets:
                # 1. 받을 물통이 비어 있다면, 현재 상태 배열을 복제
                if limit[target] - array[target]:
                    new_array = list(array)
                    # 1-1. 받을 물통에 남은 공간이 줄 물통의 물 양보다 적거나 같다면 -> 가득 찰 때까지 붓는다
                    if limit[target] - array[target] <= array[i]:
                        new_array[target] = limit[target]
                        new_array[i] = array[i] - (limit[target] - array[target])
                        # 물을 부은 상태로 다른 경우의 수 찾기
                        pour(new_array)
                    # 1-2. 받을 물통에 남은 공간이 줄 물통의 물 양보다 크다면 -> 모두 붓는다
                    else:
                        new_array[target] = array[target] + array[i]
                        new_array[i] = 0
                        # 물을 부은 상태로 다른 경우의 수 찾기
                        pour(new_array)


# C에만 가득 차 있는 상태로 경우의 수 찾기
pour([0, 0, limit[2]])
# A가 비어 있는 경우 C의 경우의 수 기록하기
case_c = []
for result in results:
    if not result[0]:
        case_c.append(result[2])
# 중복 제거
case_c = list(set(case_c))
# 정렬
case_c.sort()
# 출력
case_c = list(map(str, case_c))
print(' '.join(case_c))
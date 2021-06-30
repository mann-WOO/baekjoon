# numbers에 검색할 숫자가 존재하는지 체크하는 함수 check
def check(k, N):
    # 이분탐색
    s, e = 0, N
    while s < e:
        # 현재 탐색한 원소와 타겟이 일치한다면 끝낸다.
        mid = (s + e) // 2
        if numbers[mid] == target:
            print('1')
            return
        # 현재 탐색한 원소와 타겟이 일치하지 않는다면 대소관계에 따라 범위를 반으로 줄인다.
        else:
            if numbers[mid] < target:
                s = mid+1
            else:
                e = mid
    print('0')


# 숫자열 numbers
N = int(input())
numbers = list(map(int, input().split()))
# 검색할 숫자들의 리스트 targets
M = int(input())
targets = list(map(int, input().split()))
# numbers를 정렬
numbers.sort()
# numbers에 검색할 숫자가 존재하는지 체크
for target in targets:
    check(target, N)
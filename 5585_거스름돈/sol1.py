# 지폐 종류
bills = [500, 100, 50, 10, 5, 1]

# 예산 1000원, 물건 값 cost
budget = 1000
cost = int(input())

# 거스름돈 세기
remain = budget - cost
count = 0
for i in range(len(bills)):
    while remain >= bills[i]:
        remain -= bills[i]
        count += 1

# 결과 출력
print(count)

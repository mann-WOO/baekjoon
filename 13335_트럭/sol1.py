# 트럭 수 n, 다리 길이 w, 가용 무게 L
n, w, L = map(int, input().split())
# 트럭 무게들의 리스트 trucks
trucks = list(map(int, input().split()))

# 다리 위의 상태 배열 bridge
bridge =[0 for _ in range(w)]
# 시간의 흐름을 기록하는 count
count = 0
# trucks를 비울 때까지 반복
while trucks:
    # 다리의 가장 앞을 꺼내며 가용무게에 합산
    L += bridge.pop(0)
    # 현재 다리가 가장 앞 트럭을 수용할 수 있다면
    if L - trucks[0] >= 0:
        # 가용무게에서 트럭무게를 차감
        L -= trucks[0]
        # 다리에 트럭 추가
        bridge.append(trucks.pop(0))
    # 현재 다리가 트럭을 수용할 수 없다면 0을 추가
    else:
        bridge.append(0)
    count += 1
# 마지막 트럭이 들어가며 while문 끝나므로 마지막 트럭이 지나가는 시간 w 합산
answer = count + w
print(answer)


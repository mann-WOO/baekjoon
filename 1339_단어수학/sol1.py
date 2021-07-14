# 단어의 수 N
N = int(input())
# 알파벳 목록 chars, 각 알파벳이 곱해져야하는 값들의 목록 count
chars = []
count = []
# 각 단어를 확인
for _ in range(N):
    # 단어 입력받기
    word = input()
    # 단어의 알파벳들을 확인
    for i in range(len(word)):
        char = word[i]
        # 이미 확인한 알파벳이라면
        if char in chars:
            # count 배열의 해당 자리에 알파벳의 자릿수에 따라 곱해져야 하는 값을 합산
            idx = chars.index(char)
            count[idx] += 10**((len(word)-i)-1)
        # 확인한 적 없는 알파벳으라면 chars, count 에 신규로 추가
        else:
            chars.append(char)
            count.append(10**((len(word)-i)-1))
answer = 0
# count를 큰 순서대로 정렬
count.sort(reverse=True)
# 가장 큰수부터 시작 해 9부터 1씩 줄여가며 곱해서 정답에 더해준다.
for i in range(len(count)):
    answer += (9-i)*count[i]
# 정답 출력
print(answer)

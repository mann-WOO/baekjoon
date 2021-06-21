# 피보나치 수열로 A와 B의 string 구하기
def fibonacci(n):
    if n == 1:
        return 'a'
    if n == 2:
        return 'b'
    else:
        return fibonacci(n-2) + fibonacci(n-1)


# 피보나치 수열의 D항에 a와 b의 개수 count_a, count_b 구하기
D, K = map(int, input().split())
ab = fibonacci(D)
count_a = ab.count('a')
count_b = ab.count('b')

# a를 1부터 대입, K가 a와 b의 조합으로 나누어 떨어질 때의 a,b 값 구하기
for i in range(1, K):
    remain = K - i*count_a
    if remain % count_b == 0:
        a = i
        b = remain // count_b
        break

print(f'{a}\n{b}')

# 5086 배수와 약수
# https://www.acmicpc.net/problem/5086
while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    if M > N and M % N == 0:
        print("factor")
    elif N > M and N % M == 0:
        print("multiple")
    else:
        print("neither")
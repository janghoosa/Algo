# 10814 단어 정렬
# https://www.acmicpc.net/problem/10814
N = int(input())
A = []
for _ in range(N):
    (x, y) = input().split()
    A.append((int(x),y))
A = sorted(A, key=lambda x: x[0])
for i in A:
    print(i[0],i[1])
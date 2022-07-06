# 1436 영화감독 숌
# https://www.acmicpc.net/problem/1436
N = int(input())
tmp = '666'
i = 666

while N:
    if tmp in str(i):
        N -= 1
    i += 1

print(i-1)
# 17609 회문
# https://www.acmicpc.net/problem/17609
N = int(input())
A = [input() for _ in range(N)]
def check(x):
    pointer1 = 0
    pointer2 = len(x)-1
    res = 0
    if x == x[::-1]:
        return 0
    while pointer1 < pointer2:
        if x[pointer1] == x[pointer2]:
            pointer1 += 1
            pointer2 -= 1
            continue
        else:
            if x[pointer1+1] == x[pointer2]:
                tmp = x[pointer1+1:pointer2+1]
                if tmp == tmp[::-1]:
                    return 1
            if x[pointer1] == x[pointer2-1]:
                tmp = x[pointer1:pointer2]
                if tmp == tmp[::-1]:
                    return 1
            return 2

for i in A:
    print(check(i))
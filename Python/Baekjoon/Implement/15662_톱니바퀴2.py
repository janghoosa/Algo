# 15662 톱니바퀴 (2)
# https://www.acmicpc.net/problem/15662
from collections import deque
T = int(input())
GEAR = [deque(input()) for _ in range(T)]

def rotate(i, d):
    tmp = []
    tmpd = d
    tmp.append((i,tmpd))
    for j in range(i,T-1):
        if GEAR[j][2] != GEAR[j+1][6]:
            tmpd*= -1
            tmp.append((j+1, tmpd))
        else:
            break
    tmpd = d
    for j in reversed(range(1,i+1)):
        if GEAR[j-1][2] != GEAR[j][6]:
            tmpd *= -1
            tmp.append((j-1, tmpd))
        else:
            break
    for rol in tmp:
        GEAR[rol[0]].rotate(rol[1])


K = int(input())
A = [list(map(int, input().split())) for _ in range(K)]
for i in A:
    rotate(i[0]-1,i[1])
ans = 0
for i in GEAR:
    if i[0] == '1':
        ans += 1
print(ans)
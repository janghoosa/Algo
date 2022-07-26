# 12904 A와 B
# https://www.acmicpc.net/problem/12904
S = list(input())
T = list(input())
while len(S) < len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
if S == T:
    print(1)
else:
    print(0)
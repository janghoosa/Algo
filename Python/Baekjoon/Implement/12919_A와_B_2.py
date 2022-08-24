# 12919 A와 B 2
# https://www.acmicpc.net/problem/12919
S = list(input())
T = list(input())
ans = 0
def check(S,T):
    global ans
    if len(S) == len(T):
        if S == T:
            ans = 1
        return
    if T[-1] == 'A':
        tmp = T.pop()
        check(S, T)
        T.append(tmp)
    if T[0] == 'B':
        T.reverse()
        tmp = T.pop()
        check(S, T)
        T.append(tmp)
        T.reverse()
check(S, T)
print(ans)
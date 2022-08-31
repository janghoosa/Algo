# 2469 사다리 타기
# https://www.acmicpc.net/problem/2469
k = int(input())
n = int(input())
end = list(input())
start = sorted(end)
rows = [list(input()) for _ in range(n)]
i = 0
# ?까지 내리기
while i < n :
    if rows[i][0] == '?':
        break
    for j in range(k-1):
        if rows[i][j] == '-':
            start[j], start[j+1] = start[j+1], start[j]
    i += 1
# ?까지 올리기
for l in reversed(range(i+1, n)):
    for j in range(k-1):
        if rows[l][j] == '-':
            end[j], end[j+1] = end[j+1], end[j]

ans = ""
for j in range(k-1):
    if start[j] == end[j]:
        ans += '*'
        continue
    elif start[j] == end[j+1] and start[j+1] == end[j]:
        ans += '-'
    elif start[j-1] == end[j] and start[j] == end[j-1]:
        ans += '*'
    else:
        ans = 'x'* (k-1)
        break
print(ans)
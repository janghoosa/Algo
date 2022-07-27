# 18405 경쟁적 전염
# https://www.acmicpc.net/problem/18405
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
pkt = []
def spread(y, x):
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and A[y + dy[i]][x + dx[i]] == 0:
            A[y + dy[i]][x + dx[i]] = A[y][x]
            pkt2.append((A[y][x],y + dy[i],x + dx[i]))
    return

for i in range(N):
        for j in range(N):
            if A[j][i] != 0:
                pkt.append((A[j][i],j,i))

while S:
    pkt2 = []
    pkt.sort(reverse=True)
    for i in range(len(pkt)):
        tmp = tmp.pop()
        spread(tmp[1], tmp[2])
    S -= 1
    pkt = pkt2
print(A[X-1][Y-1])
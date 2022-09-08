# 16509 장군
# https://www.acmicpc.net/problem/16509
from collections import deque
sx , sy = map(int, input().split())
kx , ky = map(int, input().split())
visited = [[0 for _ in range(9)] for _ in range(10)]
visited[sx][sy] = 1
queue = deque([(sx, sy, 0)])
dir = [
    ([0, 1], [1, 1], [1, 1]), # ⬆️↗️↗️
    ([0, 1], [-1, 1], [-1, 1]), # ⬆️↖️↖️
    ([-1, 0], [-1, 1], [-1, 1]), # ⬅️↖️↖️
    ([-1, 0], [-1, -1], [-1, -1]), # ⬅️↙️↙️
    ([0, -1], [-1, -1], [-1, -1]), # ⬇️↙️↙️
    ([0, -1], [1, -1], [1, -1]), # ⬇️↘️↘️
    ([1, 0], [1, 1], [1, 1]), # ➡️↗️↗️
    ([1, 0], [1, -1], [1, -1]), # ➡️↘️↘️
]
while queue:
    x, y, times = queue.popleft()
    if x == kx and y == ky:
        print(times)
        break
    for i in range(8):
        dx = x
        dy = y
        for j in range(3):
            dx = dx + dir[i][j][0]
            dy = dy + dir[i][j][1]
            if dx == kx and dy == ky and j < 2:
                break
            if 0 <= dx < 10 and 0 <= dy < 9 and j == 2:
                if visited[dx][dy] != 1:
                    queue.append((dx,dy,times+1))
                    visited[dx][dy] = 1
# 13335 트럭
# https://www.acmicpc.net/problem/13335
from collections import deque
n, w, L = map(int, input().split())
truck = deque(map(int, input().split()))
queue = deque([0 for _ in range(w-1)])
first = truck.popleft()
queue.append(first)
weight = first
ans = 1
while weight > 0:
    if truck:
        tmp = truck.popleft()
        while True:
            weight -= queue.popleft()
            if weight + tmp <= L:
                queue.append(tmp)
                weight += tmp
                ans += 1
                break
            else:
                queue.append(0)
                ans += 1
    else:
        queue.append(0)
        ans += 1
        weight -= queue.popleft()
print(ans)
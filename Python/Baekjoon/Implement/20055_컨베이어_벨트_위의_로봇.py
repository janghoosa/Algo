# 20055 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055
from collections import deque
N, K = map(int,input().split())
A = deque(map(int,input().split()))
goal = A.count(0)
ans = 0
robot = deque(0 for _ in range(N))
while goal < K:
    A.appendleft(A.pop())
    robot.appendleft(robot.pop())
    robot[-1] = 0
    for i in reversed(range(N-1)):
        if robot[i] == 1 and robot[i+1] == 0 and A[i+1] > 0:
            robot[i+1] = 1
            robot[i] = 0
            A[i+1] -= 1
    robot[-1] = 0
    if A[0] > 0:
        robot[0] = 1
        A[0] -= 1
    goal = A.count(0)
    ans += 1
print(ans)
# 20056 마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056
N, M, K = map(int, input().split())
A = [[[] for _ in range(N)] for _ in range(N)]

fbs = []
for i in range(M):
    tmp = list(map(int, input().split()))
    fbs.append([tmp[0]-1,tmp[1]-1,tmp[2],tmp[3],tmp[4]])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for i in range(K):
    while fbs:
        fb = fbs.pop()
        y = fb[1]
        x = fb[0]
        direction = fb[4]
        speed = fb[3]
        nx = (x + dx[direction] * speed)%N
        ny = (y + dy[direction] * speed)%N
        A[nx][ny].append([fb[2],speed,direction])

    for y in range(N):
        for x in range(N):
            cnt = len(A[x][y])
            if cnt > 1:
                m = 0
                s = 0
                cnt_odd = 0
                cnt_even = 0
                for tmp in A[x][y]:
                    m += tmp[0]
                    s += tmp[1]
                    if tmp[2] % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1
                A[x][y] = []
                if cnt_odd == cnt or cnt_even == cnt:
                    dd = [0, 2, 4, 6]
                else:
                    dd = [1, 3, 5, 7]
                if m//5:
                    for nd in dd:
                        fbs.append([x,y,m//5, s//cnt, nd])
            
            if cnt == 1:
                fbs.append([x,y]+A[x][y].pop())
ans = 0
for fb in fbs:
    ans += fb[2]
print(ans)
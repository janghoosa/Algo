# 1360 되돌리기
# https://www.acmicpc.net/problem/1360
N = int(input())
A = [input().split() for _ in range(N)]
B = []
ans = ''
for i in range(N):
    flag = False
    func, val, time = A[i]
    time = int(time)
    if func == 'type':
        ans += val
        B.append((time, ans))
    else:
        val = int(val)
        for j in range(len(B)-1,-1,-1):
            if B[j][0] >= time - val : continue
            flag = True
            ans = B[j][1]
            B.append((time,ans))
            break
        if not flag:
            ans = ''
            B.append((time,ans))
print(ans)
            

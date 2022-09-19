# 1117 색칠
# https://www.acmicpc.net/problem/1117
W,H,f,c,x1,y1,x2,y2 = map(int, input().split())

doubledx = min(f, W-f)

if x1 <= doubledx and doubledx <= x2: # 색칠이랑 겹친 부분이 걸칠 때
    area = (x2-x1) * (y2-y1) * (c+1) + (doubledx-x1) * (y2-y1) * (c+1)
elif x1 <= doubledx and x2 <= doubledx:  # 색칠이랑 겹친 부분이 아예 겹칠 때
    area = 2 * (x2-x1) * (y2-y1) * (c+1)
else:                                    # 겹친 부분이 없을 때
    area = (x2-x1) * (y2-y1) * (c+1)
print(W*H-area)
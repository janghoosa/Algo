# 14719 빗물
# https://www.acmicpc.net/problem/14719
H, W = map(int, input().split())
A = [[0 for _ in range(W) ] for _ in range(H)]
tmp = list(map(int, input().split()))

for i in range(W):
    for j in range(tmp[i]):
        A[j][i] = 1
water = 0
for i in A:
    index = 0
    left = False
    while index < W:
        if i[index] ==1 :
            left = True
        if left:
            right = False
            while index < W :
                if i[index] == 1:
                    right = True
                    break
                water += 1
                i[index] = 2
                index += 1
            if right == False:
                index = W-1
                while i[index] == 2:
                    water -= 1
                    i[index] = 0
                    index -= 1
                break
        index += 1
                
print(water)
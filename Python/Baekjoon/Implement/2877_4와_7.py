# 2877 4와 7 
# https://www.acmicpc.net/problem/2877
N = int(input())
ans = N+1
ans = bin(ans)
ans = str(ans)
# print(ans)
for i in range(3,len(ans)):
    if ans[i] == '0':
        print(4,end='')
    else:
        print(7,end='')
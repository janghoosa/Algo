# 11478 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478
A =  input()
B = {}
cnt = 0
for i in range(len(A)):
    for j in range(i+1,len(A)+1):
        if A[i:j] not in B:
            cnt += 1
            B[A[i:j]] = 1
print(cnt)
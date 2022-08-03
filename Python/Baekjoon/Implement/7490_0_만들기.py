# 7490 0 만들기
# https://www.acmicpc.net/problem/7490
import copy
N = int(input())

def recurse(arr, m):
    if len(arr) == m:
        A.append(copy.deepcopy(arr))
        return
    arr.append(' ')
    recurse(arr, m)
    arr.pop()
    arr.append('+')
    recurse(arr, m)
    arr.pop()
    arr.append('-')
    recurse(arr, m)
    arr.pop()

def check0(req):
    tmp = str(req).replace(' ', '')
    if eval(tmp) == 0:
        print(req)


for _ in range(N):
    A = []
    M = int(input())
    recurse([],M-1)
    num = [i for i in range(1, M+1)]
    for i in A:
        string = ""
        for j in range(M-1):
            # print(i, num)
            string += str(num[j])+i[j]
        string += str(num[-1])
        check0(string)
    print('')
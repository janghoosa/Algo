# 11067 모노톤킬
# https://www.acmicpc.net/problem/11067
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    Cafe = {}
    for i in range(n):
        a, b = map(int, input().split())
        if a not in Cafe:
            Cafe[a] = list()
        Cafe[a].append(b)
    maxKey = 0
    Cafe = sorted(Cafe.items())
    rank = []
    pkey = 0
    for i in range(len(Cafe)):
        Cafe[i][1].sort()
        if Cafe[i][1][0] == pkey:
            for j in Cafe[i][1]:
                rank.append([Cafe[i][0],j])
                pkey = j
        else:
            for j in reversed(Cafe[i][1]):
                rank.append([Cafe[i][0],j])
                pkey = j
    
    a = list(map(int, input().split()))
    for i in range(1,a[0]+1):
        print(*(rank[a[i]-1]))
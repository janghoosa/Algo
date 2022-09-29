# 20159 동작 그만. 밑장 빼기냐?
# https://www.acmicpc.net/problem/20159
N = int(input())
A = list(map(int, input().split()))
odd_psum = [0] * (N//2)
even_psum = [0] * (N//2)
even_psum[0] = A[0]
odd_psum[-1] = A[-1]
for i in range(1, N//2):
    even_psum[i] = A[2*i] + even_psum[i-1]
    odd_psum[-i-1] = A[-2*i-1] + odd_psum[-i]
max_sum = 0
for i in range(len(even_psum)):
    if not i == len(odd_psum) - 1:
        max_sum = max(max_sum, even_psum[i] + odd_psum[i + 1])
    max_sum = max(max_sum, even_psum[i] + odd_psum[i] - A[-1])
max_sum = max(max_sum, even_psum[-1], odd_psum[0])
print(max_sum)
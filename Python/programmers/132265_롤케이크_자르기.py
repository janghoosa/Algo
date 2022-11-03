# 132265 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import Counter

def solution(topping):
    answer = 0
    top = max(topping)
    left = [0 for _ in range(top)]
    right = [0 for _ in range(top)]
    val_left = 0
    val_right = 0
    for key, value in Counter(topping).items():
        right[key-1] += value
        val_right += 1
    
    for topp in topping:
        right[topp-1] -= 1
        left[topp-1] += 1
        if right[topp-1] == 0:
            val_right -= 1
        if left[topp-1] == 1:
            val_left += 1
        if val_right == val_left:
            answer += 1
    
    return answer
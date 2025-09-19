# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 1번 순회 후 투포인터 문제
# 한번 순회하면서 최저가를 찾고, 그 최저가로 해당 날짜에 팔았을 때의 최대 이익을 갱신하는 방식
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pointer = 0
        min_pointer = 100000
        for price in prices:
            if price < min_pointer:
                min_pointer = price
            else:
                max_pointer = max(max_pointer, price - min_pointer)
        return max_pointer
# Majority Element
# https://leetcode.com/problems/majority-element/
# Boyer-Moore 과반수 투표 알고리즘
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
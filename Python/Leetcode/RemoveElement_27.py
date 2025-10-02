# Remove Element
# https://leetcode.com/problems/remove-element/
# 1번 순회 후 투포인터 문제
# 한번 순회하면서 val이 아닌 값들을 앞으로 당겨오는 방식
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                
        return i

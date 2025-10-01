# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 1번 순회 후 투포인터 문제
# 한번 순회하면서 중복되지 않은 값이 나올떄까지 본 후 앞으로 당겨오는 방식
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

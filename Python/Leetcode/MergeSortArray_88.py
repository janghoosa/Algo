# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# 머지소트 구현 문제
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2, total = m - 1, n - 1, m + n - 1
    
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[total] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[total] = nums2[idx2]
                idx2 -= 1
            total -= 1
    
        while idx2 >= 0:
            nums1[total] = nums2[idx2]
            idx2 -= 1
            total -= 1
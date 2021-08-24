""""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""

from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        def helper(nums1, nums2, k):
            if len(nums1) < len(nums2):
                # 保证nums2为较短的数组
                nums1, nums2 = nums2, nums1
            if len(nums2) == 0:
                return nums1[k-1]
            if k == 1:
                return min(nums1[0], nums2[0])
            t = min(k//2, len(nums2)//2)
            if nums1[t-1] <= nums2[t-1]:
                return helper(nums1[t:], nums2, k-t)
            else:
                return helper(nums1, nums2[t:], k-t)
        
        return (helper(nums1, nums2, k1) + helper(nums1, nums2, k2)) / 2

sol = Solution()
result = sol.findMedianSortedArrays([1,3,5,6,7,23], [2,54,102])
print(result)
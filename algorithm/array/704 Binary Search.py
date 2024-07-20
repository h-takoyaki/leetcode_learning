"""
https://leetcode.cn/problems/binary-search/description/
"""
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.search(nums = [-1,0,3,5,9,12], target = 2))

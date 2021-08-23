"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""

from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用hashmap将寻找target-num的时间降低到O(1)
        hashmap = dict()
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i

sol = Solution()
result = sol.twoSum(nums = [2,7,11,15], target = 9)
print(result)
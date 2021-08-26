"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boats-to-save-people
"""

from typing import *

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light, heavy = 0, len(people)-1
        boats = 0

        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light +=1
            heavy -= 1
            boats += 1
        return boats

sol = Solution()
result = sol.numRescueBoats([3,2,2,1], 3)
print(result)
from typing import *


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 利用hash表解决问题
        counters = dict()
        for num in nums:
            if counters.get(num) is not None:
                return num
            else:
                counters[num] = 1

    def findRepeatNumber2(self, nums: List[int]) -> int:
        # 利用条件在其中的数字都是0~n-1
        for i, num in enumerate(nums):
            if nums[i] == i:
                continue
            while nums[i] != i:
                if nums[num] == num:
                    return num
                else:
                    nums[num], nums[i] = nums[i], nums[num]
                    # nums[i], nums[num] = nums[num], nums[i]


def main():
    nums = [2, 3, 1]
    a = Solution()
    print(a.findRepeatNumber2(nums))


if __name__ == '__main__':
    main()

from typing import *


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    counter = {}
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
    nums = sorted(counter)
    ans, N = [], len(nums)
    for i in range(N):
        a = nums[i]
        if a * 4 > target:
            break
        if a + 3 * nums[-1] < target:
            continue
        counter[a] -= 1
        for j in range(i if counter[a] > 0 else i + 1, N):
            b = nums[j]
            if a + b * 3 > target:
                break
            if a + b + nums[-1] * 2 < target:
                continue
            counter[b] -= 1
            for k in range(j if counter[b] > 0 else j + 1, N):
                c = nums[k]
                d = target - a - b - c
                if c > d:
                    break
                if d not in counter or c == d and counter[c] < 2:
                    continue
                ans.append([a, b, c, d])
            counter[b] += 1
    return ans


class Solution:
    pass


def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    a = Solution()
    print(fourSum(nums, target))


if __name__ == '__main__':
    main()

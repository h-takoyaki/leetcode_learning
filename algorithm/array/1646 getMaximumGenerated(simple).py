class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # 注意边界状态
        nums = [0] * (n+1)
        if n == 0:
            return 0
        nums[1] = 1

        for i in range(1,n//2+1):
            if 2*i <=n:
                nums[2*i] = nums[i]
            if 2*i+1 <=n:
                nums[2*i+1] = nums[i] + nums[i+1]
        # print(nums)
        
        return max(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.getMaximumGenerated(7))
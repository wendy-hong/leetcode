class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Execution time: 60 ms, defeat 61% of all Python users
        # Memory consumption: 21.2 MB, defeat 9% of all Python users
        # Test cases passed: 202/202
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

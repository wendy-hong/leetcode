class Solution:
    def canJump_sol1(self, nums: List[int]) -> bool:
        # Execution time: 76 ms, defeat 83.85% of all Python users
        # Memory consumption: 15.5 MB, defeat 24.64% of all Python users
        # Test cases passed: 166/166
        n = len(nums)
        index = 0
        pos = 0
        while index <= pos and index < n:
            if pos >= n - 1:
                return True
            if index + nums[index] > pos:
                pos = index + nums[index]
            index += 1
        return False

    def canJump_sol2(self, nums: List[int]) -> bool:
        # Execution time: 80 ms, defeat 76.91% of all Python users
        # Memory consumption: 15.3 MB, defeat 73.81% of all Python users
        # Test cases passed: 166/166
        n = len(nums)
        pos = 0
        for i in range(n):
            if i <= pos:
                pos = max(pos, i + nums[i])
                if pos >= n - 1:
                    return True
        return False

    def canJump_sol3(self, nums: List[int]) -> bool:
        # Execution time: 80 ms, defeat 76.91% of all Python users
        # Memory consumption: 15.3 MB, defeat 75.19% of all Python users
        # Test cases passed: 166/166
        n = len(nums)
        dp = nums[0]
        for i in range(1, n):
            if dp==0:
                return False
            dp = max(dp-1, nums[i])
        return True
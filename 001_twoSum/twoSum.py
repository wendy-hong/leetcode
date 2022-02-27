class Solution:
    def twoSum_sol1(self, nums: List[int], target: int) -> List[int]:
        # Time: O(N^2), Space: O(1)
        # Execution time: 2972 ms, defeat 27.56% of all Python users
        # Memory consumption: 15.3 MB, defeat 58.70% of all Python users
        # Test cases passed: 57/57
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum_sol2(self, nums: List[int], target: int) -> List[int]:
        # Hash Table
        # Time: O(N), Space: O(N)
        # Execution time: 48 ms, defeat 51.55% of all Python users
        # Memory consumption: 15.7 MB, defeat 46.77% of all Python users
        # Test cases passed: 57/57
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return None

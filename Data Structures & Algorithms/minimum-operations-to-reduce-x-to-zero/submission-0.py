class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        total = 0
        l = 0
        len_max_window = -1

        for r in range(len(nums)):
            total += nums[r]

            while l <= r and total > target:
                total -= nums[l]
                l += 1
            
            if total == target:
                len_max_window = max(len_max_window, r -l + 1)
            
        return -1 if len_max_window == -1 else len(nums) - len_max_window


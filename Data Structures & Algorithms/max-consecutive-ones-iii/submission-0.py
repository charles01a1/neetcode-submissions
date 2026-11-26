class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_sub = 0
        l = 0 

        for r in range(len(nums)):
            k -= (1 if nums[r] == 0 else 0)

            while k < 0 and l <= r: 
                k += (1 if nums[l] == 0 else 0)
                l += 1
            max_sub = max(max_sub, r - l + 1)
        
        return max_sub
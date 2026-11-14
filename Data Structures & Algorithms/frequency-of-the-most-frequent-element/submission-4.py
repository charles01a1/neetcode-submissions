class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        total = nums[0]
        l,r = 0,0
        max_so_far = 0

        while l <= r and r < len(nums):
            max_in_window = nums[r] * (r - l + 1)
            max_we_get = total + k

            if max_in_window > max_we_get:
                total -= nums[l]
                l += 1
            else:
                r += 1
                total += nums[r] if r < len(nums) else 0 
            max_so_far = max(max_so_far, r-l)

        return max_so_far
        
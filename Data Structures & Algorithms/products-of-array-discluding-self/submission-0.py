class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [1] * len(nums)
        suff = [1] * len(nums)

        result = [None] * len(nums)

        for i,num in enumerate(nums):
            pref[i] = pref[i-1] * num

        for i,num in enumerate(reversed(nums)):
            original_index = len(nums) - 1 - i
            suff[original_index] = suff[(original_index + 1) % len(nums)] * num

        for i in range(len(nums)):
            if i - 1 < 0:
                result[i] = suff[i + 1]
            elif i + 1 >= len(nums):
                result[i] = pref[i-1]
            else:
                result[i] = pref[i-1] * suff[i+1]

        return result

        
        
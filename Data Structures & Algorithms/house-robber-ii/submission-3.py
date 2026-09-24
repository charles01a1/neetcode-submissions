class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob1(nums: List[int]) -> int:
            cache = [None for i in range(len(nums))]

            def dp(i):
                if i >= len(nums):
                    return 0

                if cache[i] != None:
                    return cache[i]
                choose = nums[i] + dp(i+2)
                not_choose = dp(i+1)

                best = max(choose, not_choose)
                cache[i] = best

                return best

            return dp(0)
            

        return max(nums[0],rob1(nums[1:]),rob1(nums[:-1]))
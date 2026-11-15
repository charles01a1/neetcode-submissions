class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        total, res = 0, float("inf")

        for r in range(len(nums)):
            total += nums[r]

            if total >= target:
                while l <=r and (total - nums[l]) >= target:
                    total -= nums[l]
                    l += 1

                res = min(res, r - l + 1)

        return res if res != float("inf") else 0

        # prefix_sum = [0] * len(nums) + 1
        # for i in range(len(nums)):
        #     prefix_sum[i+1] = prefix_sum[i] + nums[i]

        # l,r = 0,len(nums)
        # mid = (l + r) // 2
    
        # if nums[mid] < target:
        #     l = mid + 1
        # else:
        #     r = mid - 1

        # l
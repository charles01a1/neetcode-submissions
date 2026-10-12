class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        last_index = len(nums)-1
        cur_min, cur_max = nums[last_index], nums[last_index]
        max_res = nums[last_index]

        for i in range(len(nums)-2,-1,-1):
            temp_min = cur_min

            cur_min = min(nums[i], nums[i] * cur_min, nums[i] * cur_max)
            cur_max = max(nums[i], nums[i] * temp_min, nums[i] * cur_max)

            max_res = max(max_res, cur_max)

        return max_res
        
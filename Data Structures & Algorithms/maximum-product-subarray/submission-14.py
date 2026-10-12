class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        last_index = len(nums)-1
        cur_min, cur_max = nums[last_index], nums[last_index]
        max_res = nums[last_index]

        for i in range(len(nums)-2,-1,-1):
            # if nums[i] < -1:
            temp_min = cur_min

            cur_min = min(nums[i], nums[i] * cur_min, nums[i] * cur_max)
            cur_max = max(nums[i], nums[i] * temp_min, nums[i] * cur_max)

            # print("after ", cur_min, cur_max)

            max_res = max(max_res, cur_max)
            # LSE[i] = [min_no,max_no]

            # max_result = max(max_result, max_no, min_no)

            # print(i, cur_min, cur_max)


        # print(LSE)
        return max_res
        
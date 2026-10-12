class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        LSE = [[0,0]] * len(nums)
        last_index = len(nums)-1
        LSE[last_index] = [nums[last_index], nums[last_index]]

        max_result = nums[last_index]

        for i in range(len(nums)-2,-1,-1):
            # if nums[i] < -1:
            min_no = min(nums[i], nums[i] * LSE[i+1][0], nums[i] * LSE[i+1][1])
            max_no = max(nums[i], nums[i] * LSE[i+1][1], nums[i] * LSE[i+1][0])
            LSE[i] = [min_no,max_no]

            max_result = max(max_result, max_no, min_no)


        # print(LSE)
        return max_result
        
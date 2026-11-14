class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        results = 0

        for i in range(len(nums)):
            if (nums[i] * 2) <=  target:
                last_index = self.binary_search(i, nums, target)
                results += (2 ** (last_index - i))

        return results % ((10 ** 9) + 7)

    def binary_search(self,i, nums, target):
        l,r = i, len(nums) - 1 

        while l <= r:
            mid = (l + r) // 2

            if nums[i] + nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return r

            

                
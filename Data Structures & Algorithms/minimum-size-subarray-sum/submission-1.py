class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        n = len(nums)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]


        res = n + 1
        for i in range(n):
            l,r = 0,i

            while l <= r:
                mid = (l + r) // 2
                current_sum = prefix_sum[i + 1] - prefix_sum[mid]
            
                if current_sum >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            if r >= 0:
                res = min(res, i - r + 1)
        
        return res % (n + 1)


            

                    

            
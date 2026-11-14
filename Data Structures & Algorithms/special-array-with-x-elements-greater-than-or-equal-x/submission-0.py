class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l,r = 0, max(nums)

        while l<=r:

            mid = (l + r ) // 2 
            current = sum(1 if n >= mid else 0 for n in nums)

            if current == mid:
                return mid

            elif current > mid:
                l = mid + 1
            else:
                r = mid - 1
        

        return -1
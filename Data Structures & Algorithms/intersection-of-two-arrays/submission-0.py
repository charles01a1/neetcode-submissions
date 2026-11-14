class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        results = set()
        nums1.sort()
        nums2.sort()

        for num in nums1:
            if self.binary_search(num, nums2):
                results.add(num)
        
        return list(results)


    def binary_search(self,num, nums2):
        l,r = 0, len(nums2) -1 

        while l <= r:

            mid = (l + r) // 2
            
            if nums2[mid] == num:
                return True
            elif nums2[mid] > num:
                r = mid - 1
            else:
                l = mid + 1

        return False
        
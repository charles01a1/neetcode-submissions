class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        length = 1
        result = 0

        for num in nums:
            if (num - 1) not in hash_set:
                length = 1
                while (num + 1) in hash_set:
                    length += 1
                    num += 1
                
                result = max(result,length)


        return result
            
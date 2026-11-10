class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)

        for num in nums:
            store[num] += 1

        sorted_list =  sorted(store.items(), key = lambda x:-x[1])[:k]

        return [ key[0] for key in sorted_list]
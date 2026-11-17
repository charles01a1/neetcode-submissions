class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arrs = []

        for num in arr:
            arrs.append([abs(num-x),num])

        heapq.heapify(arrs)

        result = []
        for i in range(k):
            result.append(heapq.heappop(arrs)[1])

        return sorted(result)
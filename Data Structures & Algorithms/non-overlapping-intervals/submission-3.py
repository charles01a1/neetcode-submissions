class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair:pair[0])

        
        results = [intervals[0]]

        for i,j in intervals[1:]:
            if i < results[-1][1] and j < results[-1][1]:
                results[-1] = [i,j]
            elif i >= results[-1][1]:
                results.append([i,j])

        print(intervals)
        print(results)
        return len(intervals) - len(results)
                

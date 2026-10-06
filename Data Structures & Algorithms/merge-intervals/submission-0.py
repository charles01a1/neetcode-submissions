class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        results = [intervals[0]]

        for i,j in intervals[1:]:
            if i <= results[-1][1]:
                temp = results[-1]
                results[-1] = [
                    min(i,temp[0]),
                    max(j,temp[1])
                ]
            # elif 

            else:
                results.append([i,j])

        
        return results

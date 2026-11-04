import collections
class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.store.get(key,[])
        values.append([value,timestamp])
        self.store[key] = values
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        return self.binary_search(values,timestamp)

    
    def binary_search(self,values,timestamp):
        l,r = 0,len(values)-1
        largest_idx = None

        while l <= r:
            mid = (l + r) // 2

            if timestamp < values[mid][1]:
                r = mid - 1
            elif timestamp > values[mid][1]:
                l = mid + 1
                largest_idx = mid
            else:
                return values[mid][0]

        if largest_idx == None:
            return ""
        return values[largest_idx][0]


        

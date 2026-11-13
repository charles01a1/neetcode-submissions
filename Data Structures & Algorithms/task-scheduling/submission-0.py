class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        items = Counter(tasks)
        max_heap = [-cnt for cnt in items.values()]
        heapq.heapify(max_heap)
        queue = deque()

        time = 0 

        while queue or max_heap:
            time += 1

            if max_heap:
                item = 1 + heapq.heappop(max_heap)
                if item < 0:
                    queue.append([item, n + time])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap,queue.popleft()[0])

        return time
        
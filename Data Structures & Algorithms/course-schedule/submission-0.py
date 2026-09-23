class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i:[] for i in range(numCourses)}

        for cur, pre_req in prerequisites:
            preMap[cur].append(pre_req)

        visited = set()

        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur] == []:
                return True

            visited.add(cur)
            for pre_req in preMap[cur]:
                if not dfs(pre_req):
                    return False

            visited.remove(cur)
            preMap[cur] = []
            return True


        for cur in range(numCourses):
            if not dfs(cur): return False
        
        return True

    
        
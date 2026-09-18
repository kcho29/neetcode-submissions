class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # looking for cycles in a graph: use floyd's cycle detection
        # First map the graph:
        if not prerequisites:
            return True

        cmap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            cmap[course].append( prereq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if not cmap[course]:
                return True
            
            visiting.add(course)

            for p in cmap[course]:
                if not dfs(p):
                    return False
                
            visiting.remove(course)
            cmap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
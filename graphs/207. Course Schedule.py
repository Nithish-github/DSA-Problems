class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #hashmap to create the track of crs and it's preq
        premap = defaultdict(list)
        for crs,preq in prerequisites:
            premap[crs].append(preq)


        #visited set to track the cycle present the graph
        visited = set()
        def dfs(crs):

            if crs in visited:
                return False

            if premap[crs] == []:
                return True


            visited.add(crs)

            for pre in premap[crs]:
                if not dfs(pre): return False

            visited.remove(crs)
            premap[crs] = []

            return True



        for crs in range(numCourses):
            if not dfs(crs): return False

        return True


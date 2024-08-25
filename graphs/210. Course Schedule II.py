class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #needed to create a adjList 
        premap = defaultdict(list)
        for crs , pre in prerequisites:
            premap[crs].append(pre)


        output = [] 
        visited , cycle = set() , set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:  #this is the difference from course  schedule 1
                return True

            cycle.add(crs)
            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False


            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True


        for crs in  range(numCourses):
            if dfs(crs) == False:
                return []

        return output
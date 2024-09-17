class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        #It is a Topological sort problem 
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for reci , ingredient in zip(recipes , ingredients):
            indegree[reci] = len(ingredient)
            for ing in ingredient:
                graph[ing].append(reci)


        #implementing breath first search approch 
        queue = deque(supplies)
        recipes = set(recipes)
        ans = []

        while queue:

            supply  = queue.popleft()

            if supply in recipes:
                ans.append(supply) 

            for reci in graph[supply]:
                indegree[reci]-=1

                if indegree[reci] == 0:
                    queue.append(reci)

        return ans

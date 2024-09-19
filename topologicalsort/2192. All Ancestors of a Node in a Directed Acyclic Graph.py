class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # Step 1: Build the graph (adjacency list) and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: Topological Sort (using Kahn's algorithm)
        topo_order = []
        queue = deque()

        # Nodes with in-degree 0 can be processed first
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 3: Prepare a list of sets to store ancestors for each node
        ancestors = [set() for _ in range(n)]   

        for node in topo_order:

            for nei in graph[node]:
                ancestors[nei]|=ancestors[node]  #inherit the ancestors nodes
                ancestors[nei].add(node) # current node is also ancestor


        result = [sorted(list(anc)) for anc in ancestors]

        return result
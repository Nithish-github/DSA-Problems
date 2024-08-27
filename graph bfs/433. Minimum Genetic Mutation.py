class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        #this is the typical graph problem 
        if endGene not in bank: return -1

        bank = set(bank)
        genes = set(['A','C','G','T'])

        q = deque([startGene])
        visited = set([startGene])
        count = 0 


        while q:

            size = len(q)

            for _ in range(size):
                node  = q.popleft()

                if node == endGene: return count 

                for i in range(8):

                    for gene in genes:

     
                        new = sys.intern(node[:i]) + gene + sys.intern(node[i+1:])

                        if new in bank and new not in visited:
                            q.append(new)
                            visited.add(new)


            count+=1

        return -1

        
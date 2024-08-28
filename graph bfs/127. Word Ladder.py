class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #check for the end word
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern  = word[:j] +"*" +word[j+1:]
                nei[pattern].append(word)


        #Constructing the bfs   
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:

            for i in range(len(q)):
                word = q.popleft()

                #check if we had reached the end point
                if word == endWord:
                    return res

                #run the loop for the length of the words and its possibilities
                for j in range(len(word)):
                    pattern  = sys.intern(word[:j]) +"*"+ sys.intern(word[j+1:]) 
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)


            res+=1


        return 0    

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        '''
        Solution using stack datastructure
        '''

        stack = []
        cur = ""

        for i in path+"/":
            #first base condition
            if i == "/":

                if cur == "..":
                    if stack:stack.pop()
                elif cur!="" and cur!=".":
                    stack.append(cur)

                cur = ""

            else:

                cur+=i


        return "/"+"/".join(stack)



# Input: path = "/home/"

# Output: "/home"

# Explanation:

# The trailing slash should be removed.

        
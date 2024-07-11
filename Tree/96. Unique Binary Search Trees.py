class Solution:
    def numTrees(self, n: int) -> int:

        '''
        Catalan Number     C_n = (2n)! / ((n + 1)! * n!)
        '''
        catalan_number  = math.comb(2 * n , n) // (n+1)

        return catalan_number



# Input: n = 3
# Output: 5

# Example 2:

# Input: n = 1
# Output: 1

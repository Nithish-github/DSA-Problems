class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        '''
        Using the sliding window technique
        '''
        n = len(code)
        if k == 0:
            return [0] * n
        
        res = [0] * n
        step = 1 if k > 0 else -1
        k = abs(k)
        
        for i in range(n):
            window_sum = 0
            for j in range(1, k + 1):
                window_sum += code[(i + step * j) % n]
            res[i] = window_sum
        
        return res

# Sample input
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
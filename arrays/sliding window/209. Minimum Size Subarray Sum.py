class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Sliding Window Technique
        '''

        left  = 0
        total = 0
        min_length = float('inf')
        for right in range(len(nums)):
            total+=nums[right]

            while total >= target:
                min_length =min(right - left + 1, min_length)
                total-=nums[left]
                left+=1

        return 0 if min_length == float("inf") else min_length

        

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
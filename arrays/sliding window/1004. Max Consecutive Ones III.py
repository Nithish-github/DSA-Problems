class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        '''
        Sliding Window Solution
        '''
        left = 0 
        num_zeros = 0
        max_width = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros+=1

            while num_zeros >k:
                if nums[left] == 0:
                    num_zeros-=1
                left+=1
                
            max_width = max(max_width , right - left +1)

        return max_width


# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
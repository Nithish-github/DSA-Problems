class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        #Needed to use the Kadane's Algorithm here

        #One key point to remember is the array is cyclic 
        #So needed to have the concept of globmax and globMin

        currMax , currMin = 0 , 0
        globMax , globMin =  nums[0] , nums[0]
        total = 0

        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            total += n
            globMax = max(globMax , currMax)
            globMin = min(globMin , currMin)

        
        return max(globMax , total - globMin) if globMax>0 else globMax


'''

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

'''
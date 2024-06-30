class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #The rule is simple if the current sum turns negative don't consider that.
        #In this Problem we will be usign the variation of Kadane's Algorithm 
        #with sliding window technique

        currentSum = 0 
        maxSum = nums[0]
        maxL , maxR = 0 ,0
        L=0 #pointers to have the track

        for R in range(len(nums)):

            #core logic
            if currentSum < 0:
                currentSum = 0 
                L= R

            currentSum += nums[R]

            if currentSum > maxSum:
                maxSum = currentSum
                maxL , maxR = L , R


        return maxSum


# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.



            

        
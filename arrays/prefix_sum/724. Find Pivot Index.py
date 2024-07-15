class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        This algo can be solved using prefix sum approch
        '''
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum  = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i

            leftSum +=nums[i]

        return -1

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
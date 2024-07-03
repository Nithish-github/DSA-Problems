class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        '''
        Using Kadane's Algorithm 
        '''
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]

            # If the current number is negative, swap max_product and min_product
            if num < 0:
                max_product, min_product = min_product, max_product

            # Update max_product and min_product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Update the result
            result = max(result, max_product)

        return result



# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
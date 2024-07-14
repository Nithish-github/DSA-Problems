class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        Two Pointer approch
        '''
        res = []
        nums.sort()

        for i , a in enumerate(nums):

            #base condition to check the repetative element
            if i>0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l<r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l+=1

                elif threeSum > 0:
                    r-=1

                else:
                    res.append([a , nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1


        return res



# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
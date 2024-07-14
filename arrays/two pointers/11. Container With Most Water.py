class Solution:
    def maxArea(self, height: List[int]) -> int:

        '''
        Solution Using two pointer approch
        '''

        max_area = 0
        l = 0 #left pointer
        r = len(height)-1 #right pointer

        while l<r:

            current_area = (r-l) * min(height[l] , height[r])

            max_area = max(current_area , max_area)

            if height[l] < height[r]:
                l+=1

            else:
                r-=1

        return max_area
        

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
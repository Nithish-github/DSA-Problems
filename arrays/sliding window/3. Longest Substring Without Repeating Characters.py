class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Applying the sliding window concept
        '''

        left  = 0 
        charSet = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1


            charSet.add(s[right])
            max_length = max(right - left +1,max_length)

        return max_length


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.


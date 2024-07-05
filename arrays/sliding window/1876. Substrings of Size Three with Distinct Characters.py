class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        left = 0 
        right = 2 
        count = 0

        while right <len(s):
            charset = set()
            for i in range(left , right+1):
                if s[i] not in charset:
                    charset.add(s[i])
                else:
                    pass

            if  len(charset) == 3:
                count +=1

            left+=1
            right+=1

        return count

      
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
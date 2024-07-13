class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        #using list short hand method to correct the given string 

        s = [i.lower() for i in s if i.isalnum()]

        return all(s[~i]==s[i] for i in range(len(s)//2))
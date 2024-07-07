class Solution:
    def isValid(self, s: str) -> bool:

        '''
        This is the typical graph example
        '''

        stack = []

        barc = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for i in s:

            if i in barc:
                stack.append(i)

            elif stack == [] or i!=barc[stack.pop()]:
                return False


        return len(stack) == 0

# Example 1:

# Input: s = "()"
# Output: true

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        Using stack concept
        '''

        stack = []

        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())

            elif i == '-':
                a,b = stack.pop() , stack.pop()
                stack.append(b - a)

            elif i == '*':
                stack.append(stack.pop() * stack.pop())

            elif i == "/":
                a ,b = stack.pop() , stack.pop()
                stack.append(int(b/a))

            else:
                i = int(i)
                stack.append(i)


        return stack.pop()


            
        
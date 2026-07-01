class Solution:
    def isValid(self, s: str) -> bool:
        # I remember this problem, this is solved using stack
        # LIFO (Last In First Out), iterate through and
        # put the parenthesis into a stack in sequence you see them
        # if you see any closing parenthesis, then check if the top 
        # of the stack contained its opening parenthesis, 
        # if yes: stack.pop(), if no: return False
        # at the end, if valid parenthesis, the stack should be empty

        ref = {')':'(', '}':'{', ']':'['}
        stack = []

        for brkt in s:
            if brkt not in ref:
                stack.append(brkt)
            else:
                if stack and (ref[brkt] == stack[-1]):
                    stack.pop()
                else:
                    return False
        return not stack


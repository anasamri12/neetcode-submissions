class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for char in s:

            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False

                check = stack.pop()
                if check == '(' and char != ')':
                    return False
                elif check == '{' and char != '}':
                    return False
                elif check == '[' and char != ']':
                    return False
        
        return len(stack) == 0
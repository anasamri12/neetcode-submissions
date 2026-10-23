class Solution:
    def isValid(self, s: str) -> bool:
        check = []
   
        for char in s:
            if char == '(':
                check.append(')')
            elif char == '{':
                check.append('}')
            elif char == '[':
                check.append(']')
            elif not check or check.pop() != char:
                return False 

        return len(check) == 0
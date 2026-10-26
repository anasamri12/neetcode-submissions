class Solution:
    seen = []
    def isValid(self, s: str) -> bool:
        seen = []
        for char in s:
            if char == '(':
                seen.append(')')
            elif char == '{':
                seen.append('}')
            elif char == '[':
                seen.append(']')
            elif not seen or char != seen.pop():
                return False

        return not seen


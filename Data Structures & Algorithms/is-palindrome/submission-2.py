class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        rev = cleaned[::-1]
        print(cleaned)
        print(rev)
        if rev == cleaned:
            return True
        else:
            return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        checked = ""



        for char in s:
            if char.isalnum():
                checked += char.lower()

        
        return checked == checked[::-1]
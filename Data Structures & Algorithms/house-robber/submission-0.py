class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for amount in nums:
            current = max(prev1, prev2 + amount)

            prev2 = prev1
            prev1 = current

        return prev1

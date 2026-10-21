class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            comb = numbers[left] + numbers[right]
            if comb == target:
                return [left + 1, right + 1]
            elif comb < target:
                left += 1
            elif comb > target:
                right -= 1
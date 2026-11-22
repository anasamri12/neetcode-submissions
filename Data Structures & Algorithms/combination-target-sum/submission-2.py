class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i, total):
            if total == target:
                result.append(path.copy())
                return

            elif total > target or i >= len(nums):
                return

            path.append(nums[i])

            backtrack(i, total + nums[i])

            path.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return result
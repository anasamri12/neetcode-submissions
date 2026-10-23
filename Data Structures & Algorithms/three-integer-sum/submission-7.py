
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        i = 0

        while i < len(nums) - 2:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                comb = nums[i] + nums[left] + nums[right]

                if comb < 0:
                    left += 1

                elif comb > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

            i += 1

        return result

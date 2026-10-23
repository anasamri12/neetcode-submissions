class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        low, high = 0, len(nums) - 1

        for i in range(len(nums)):
            mid = low + ((high - low)//2)
            print(mid)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid

        return -1
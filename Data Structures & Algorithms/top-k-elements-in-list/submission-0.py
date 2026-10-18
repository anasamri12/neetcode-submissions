class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = dict()
        for i in range(len(nums)):
            
            
            if nums[i] in topk:
                topk[nums[i]] += 1
            else:
                topk[nums[i]] = 1
        sorted_nums = sorted(topk, key=topk.get, reverse=True)
        print(sorted_nums)
        return sorted_nums[:k]
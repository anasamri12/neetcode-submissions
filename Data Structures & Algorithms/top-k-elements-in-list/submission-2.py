class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1
        
        
        sort = sorted(dict, key=dict.get, reverse=True)
        print(sort)
        return sort[:k]
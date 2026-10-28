class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in range(len(strs)):
            sort_i = ''.join(sorted(strs[i]))
            if sort_i in result:
                result[sort_i].append(strs[i])
            else:
                result[sort_i] = [strs[i]]
    
        return list(result.values())
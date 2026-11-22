class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            sort = ''.join(sorted(word))
            if sort in res:
                res[sort].append(word)
            else:
                res[sort] = [word]


        return list(res.values())
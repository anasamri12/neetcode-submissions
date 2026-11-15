class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in seen:
                seen[sorted_word].append(i)
            else:
                seen[sorted_word] = [i]

        
        return list(seen.values())
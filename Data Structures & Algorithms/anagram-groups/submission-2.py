class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(list(strs[i])))
            if sorted_str not in group:
                group[sorted_str] = [strs[i]]
            else:
                group[sorted_str].append(strs[i])
        ans = list(map(list, group.values()))
        return ans
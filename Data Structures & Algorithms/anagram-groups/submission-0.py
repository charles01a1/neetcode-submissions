class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))
            results[sorted_str].append(string)

        sub_arrays = [values for values in results.values()]

        return sub_arrays
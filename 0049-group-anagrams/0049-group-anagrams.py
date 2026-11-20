class Solution(object):
    
    def groupAnagrams(self, strs):
        d = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in d:
                d[key] = []

            d[key].append(s)

        return list(d.values())


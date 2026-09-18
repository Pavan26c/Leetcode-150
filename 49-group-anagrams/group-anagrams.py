from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        agram=defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1

            key=tuple(count)
            agram[key].append(s)

        return list(agram.values())
               


        
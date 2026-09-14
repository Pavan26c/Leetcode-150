from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_hash= Counter(s)
        t_hash= Counter(t)

        for i in s_hash:
            if s_hash[i]!=t_hash[i]:
                return False

        return True
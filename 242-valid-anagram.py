class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cacheS = {}
        cacheT = {}
        for i in s:
            if i in cacheS:
                cacheS[i] += 1
                continue

            cacheS[i] = 1

        for i in t:
            if i in cacheT:
                cacheT[i] += 1
                continue

            cacheT[i] = 1

        if len(cacheS) != len(cacheT):
            return False

        for k, v in cacheS.items():
            if k not in cacheT or cacheT[k] != v:
                return False

        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dct_1 = {}
        dct_2 = {}
        for i_s in range(len(s)):
            if s[i_s] in dct_1.keys() : dct_1[s[i_s]] += 1
            else: dct_1[s[i_s]] = 1
            
            if t[i_s] in dct_2.keys() : dct_2[t[i_s]] += 1
            else: dct_2[t[i_s]] = 1

        for key in dct_1.keys():
            if key not in dct_2.keys(): return False
            elif dct_1[key] != dct_2[key]: return False
        return True
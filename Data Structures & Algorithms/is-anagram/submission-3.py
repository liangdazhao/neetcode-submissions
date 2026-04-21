class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic1 = {}

        for char in s:
            if char not in dic:
                dic[char] = 1
            else: 
                dic[char] += 1

        for c in t:
            if c not in dic1:
                dic1[c] = 1
            else: 
                dic1[c] += 1

        return dic == dic1

                        

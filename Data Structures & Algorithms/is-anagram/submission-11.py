class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}

        for c in s:
            if c in dicS:
                dicS[c] += 1
            else:
                dicS[c] = 0
    
        for c in t:
            if c in dicT:
                dicT[c] +=1
            else:
                dicT[c] = 0
            
        return dicS == dicT


                        

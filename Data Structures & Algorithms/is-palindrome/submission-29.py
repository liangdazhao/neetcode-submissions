class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join([c for c in s if c.isalnum()]).lower()

        l, r=0,len(res)-1

        while l<r:
            if res[l] != res[r]:
                return False
            l+=1
            r-=1
        
        return True
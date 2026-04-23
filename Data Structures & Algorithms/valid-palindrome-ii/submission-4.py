class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = ''.join([c for c in s])
        l, r = 0, len(res)-1

        while l<r:
            if s[l]!=s[r]:
                skipL, skipR = res[l+1:r+1], res[l:r]
                return (skipL == skipL[::-1]) or (skipR == skipR[::-1])
            l+=1
            r-=1
        return True
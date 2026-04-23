class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = ''.join([char for char in s])

        l, r = 0, len(res)-1

        while l<r:
            if res[l] != res[r]:
                skipL, skipR = res[l+1:r+1], res[l:r]
                return (skipL == skipL[::-1]) or (skipR == skipR[::-1])
            l+=1
            r-=1
        return True
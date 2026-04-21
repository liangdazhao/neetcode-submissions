class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join([char for char in s if char.isalnum()]).lower()
        i = 0
        end = len(res) - 1

        while i < end:
            if res[i] != res[end]:
                return False
            i += 1
            end -= 1
        return True
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 1

        while l<len(nums):
            while r<len(nums):
                if (nums[l] == nums[r]) and (abs(l-r) <= k):
                    return True 
                r+=1
            l+=1
            r = l + 1
        return False


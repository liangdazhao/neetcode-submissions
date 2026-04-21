class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            remain = target - n 
            if remain in dic:
                return [dic[remain],i]
            else:
                dic[n] = i
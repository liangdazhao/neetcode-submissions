class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 0

        return sorted(dic, key=dic.get, reverse=True)[0]
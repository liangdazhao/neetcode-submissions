class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}

        sum = 0 

        for index, number in enumerate(nums):
            remainder = target - number
            if remainder in numsDic:
                return [numsDic[remainder], index]
            else:
                numsDic[number] = index

           
        
                
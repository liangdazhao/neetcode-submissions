class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}        

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in numbers:
                return [i+1, numbers.index(diff)+1]
            

        
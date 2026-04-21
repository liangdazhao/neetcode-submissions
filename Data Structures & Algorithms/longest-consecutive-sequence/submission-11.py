class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        leng = 0

        for i in res:
            if i - 1 not in res:
                j = i
                while j in res:
                    j+=1
                leng = max(leng, j - i)  
        
        return leng


        
     
        

    
        
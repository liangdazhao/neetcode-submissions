class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []  
        maxRight = []
        res = []
        curMax = 0


        for i, n in enumerate(height):
            curMax = max(curMax, n)
            maxLeft.append(curMax)
            
        curMax = 0
            
        for i in range(len(height)-1,-1,-1):
            curMax = max(curMax, height[i])
            maxRight.insert(0,curMax)

        for i in range(len(maxLeft)):
            minHeight = min(maxLeft[i], maxRight[i])
            res.append(minHeight - height[i])

        return sum(res)
            
    

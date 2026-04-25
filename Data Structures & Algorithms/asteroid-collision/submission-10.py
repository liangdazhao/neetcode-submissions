class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] > abs(a):
                    alive = False
                    break
                elif stack[-1] < abs(a):
                    stack.pop()
                else:
                    stack.pop()
                    alive=False
                    break
        
            if alive:
                stack.append(a)
        return stack
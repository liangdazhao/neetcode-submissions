class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            stack = []

            for c in tokens:
                match c:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "-":
                        a, b = stack.pop(), stack.pop()
                        stack.append(b-a)
                    case "/":
                        a, b = stack.pop(), stack.pop()
                        stack.append(int(b/a))
                        
                if c not in ['+','*','-','/']:
                    stack.append(int(c))

            return stack[0]
            
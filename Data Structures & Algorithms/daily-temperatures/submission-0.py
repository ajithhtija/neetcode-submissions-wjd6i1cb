from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([])
        ans = [0]
        n = len(temperatures)
        stack.append((temperatures[n-1],n-1))
        j = n-2
        while j>=0:
            while stack and stack[-1][0]<=temperatures[j]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][1]-j)
            stack.append((temperatures[j],j))
            j-=1
        return ans[::-1]

        
        
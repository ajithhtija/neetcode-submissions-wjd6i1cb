from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque([])
        arr = []
        n = len(position)
        if n==1:
            return 1
        fleets = 0
        for i in range(0,n):
            arr.append((position[i],speed[i]))
        arr.sort(key = lambda a: a[0])
        stack.append(arr[-1])
        j = n-2
        while j>=0:
            curr = arr[j]
            top = stack.pop()
            currtime = (target-curr[0])/curr[1]
            toptime = (target-top[0])/top[1]
            if currtime<=toptime:
                stack.append(top)
            else:
                fleets+=1
                stack.append(curr)
            j-=1
        fleets+=1
        return fleets


        

        
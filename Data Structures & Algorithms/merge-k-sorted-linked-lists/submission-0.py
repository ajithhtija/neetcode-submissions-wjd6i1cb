# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = None
        for curr in lists:
            heapq.heappush(heap,(curr.val,id(curr),curr))
        while heap:
            curr = heapq.heappop(heap)
            if head==None:
                head = curr[2]
                c = head
                if head.next != None:
                    heapq.heappush(heap,(head.next.val,id(head.next),head.next))
            else:
                c.next = curr[2]
                if curr[2].next!=None:
                    heapq.heappush(heap,(curr[2].next.val,id(curr[2].next),curr[2].next))
                c = c.next
        return head



        
        
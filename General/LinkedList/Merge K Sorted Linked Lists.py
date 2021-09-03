# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = curr = ListNode(0)
        
        class Wraper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put(Wraper(l))
        
        while not q.empty():
            node = q.get().node
            curr.next = node
            curr = curr.next
            if node.next:
                q.put(Wraper(node.next))
        
        return head.next
        """
        merged2 = None
        
        for l in lists:
            merged2 = self.mergeTwoLists(merged2, l)
        
        return merged2
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        while (l1 and l2):
          
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next
        """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.ans = None
        def rec(curr, prev):
            if (curr == None):
                self.ans = prev
                return
            rec(curr.next, curr)
            curr.next = prev
        
        rec(head, None)
        return self.ans
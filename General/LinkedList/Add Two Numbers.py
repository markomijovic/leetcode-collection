# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        r = 0
        n1, n2, t_ans = l1, l2, ans
        
        while(n1 or n2):
            if n1 == None:
                n1 = ListNode()
            elif n2 == None:
                n2 = ListNode()
            
            _sum = n1.val + n2.val + r
            r = 0
            if _sum >= 10:
                r = 1
                _sum -= 10
            
            t_ans.val = _sum
            n1 = n1.next
            n2 = n2.next
            if n1 or n2:
                t_ans.next = ListNode()
                t_ans = t_ans.next
            elif r == 1:
                t_ans.next = ListNode(val=1)
            
        return ans
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, curr = None, head
        
        while k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        return prev
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        curr = head
        
        while count < k and curr:
            curr = curr.next
            count += 1
        
        if count == k:
            reversedHead = self.reverseLL(head, k)
            head.next = self.reverseKGroup(curr, k)
            return reversedHead
        return head
        
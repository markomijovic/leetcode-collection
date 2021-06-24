"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        if head.next == None: return head
        c = 1
        
        temp = ListNode(val=0, next=head)
        previous = temp
        # set previous to the node prior to left for the end
        while c < left:
            previous = previous.next
            c += 1
        
        current = previous.next # start point
        next = current.next
        while c < right:
            tmp = current
            current = next
            next = current.next
            current.next = tmp
            c += 1
        
        # set the edges in order
        previous.next.next = next
        previous.next = current
        return temp.next
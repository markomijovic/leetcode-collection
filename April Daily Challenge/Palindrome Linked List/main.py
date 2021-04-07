# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def __init__(self):
        self.isPal = True
        
    def isPalindrome(self, head: ListNode) -> bool:
        
        self.helper(head, head)
        return self.isPal
        
    
    def helper(self,left, right):
        
        # when I hit utmost right none skip it
        # if i find non matching values unwind recursion
        if (right is None or not self.isPal):
            return left
        
        left = self.helper(left, right.next) # say its [1, 2, 3, 3, 2, 1] -> first check if 1 != 1 -> return 2 -> unwind recursion once -> left=2,right=2 -> and so on
        
        if (left.val != right.val):
            self.isPal = False
        
        return left.next
        
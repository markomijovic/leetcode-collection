# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        n = count_len(head)
        self.head = head
        return self.recursive_bst(n)
    
    def recursive_bst(self, n):
        
        if n <= 0:
            return None
        left = self.recursive_bst(int(n/2))
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.recursive_bst(n - int(n/2) - 1)
        return root
        
        
def count_len(head):
    count = 0
    temp = head
    while (temp != None):
        temp = temp.next
        count += 1
    return count
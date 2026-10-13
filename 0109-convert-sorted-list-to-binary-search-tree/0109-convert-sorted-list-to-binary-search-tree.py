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
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle node (slow), keeping track of the node before it (prev)
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect left half from middle
        prev.next = None
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)      # left half: head...prev
        root.right = self.sortedListToBST(slow.next)  # right half: after middle
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Map each value to its index in inorder for O(1) lookup
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            # Find split point in inorder
            mid = inorder_index[root_val]
            
            # Build right subtree first (matches postorder order: left, right, root — reversed)
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            
            return root
        
        return build(0, len(inorder) - 1)
        
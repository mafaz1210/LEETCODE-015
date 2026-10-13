# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Map each value to its index in inorder for O(1) lookup
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Find split point in inorder
            mid = inorder_index[root_val]
            
            # Build left subtree first (matches preorder order: root, left, right)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)
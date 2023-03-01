# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        treeHeight = self.Height(root)
        return False if treeHeight == -1 else True
    
    
    
    def Height(self, root):
        if root == None:
            return 0
        leftHeight = self.Height(root.left)
        rightHeight = self.Height(root.right)
        #if any side is unbalanced, return false
        if leftHeight<0 or rightHeight <0 or abs(leftHeight - rightHeight) >1:
            return -1
        return max(leftHeight, rightHeight) + 1 
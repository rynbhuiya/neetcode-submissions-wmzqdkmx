# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.checkDepth(root)

        return True if res >= 0 else False
    
    def checkDepth(self, root):
        if not root:
            return 0
        
        leftTree = self.checkDepth(root.left)
        rightTree = self.checkDepth(root.right)

        if abs(leftTree - rightTree) > 1:
            return float('-inf')
        else:
            return max(leftTree, rightTree) + 1
        
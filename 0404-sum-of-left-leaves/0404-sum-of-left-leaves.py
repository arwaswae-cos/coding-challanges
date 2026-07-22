# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        if root!=None and root.left!=None and root.left.left == None and root.left.right == None:
            summ += root.left.val
        if root == None:
            return 0
        summ += self.sumOfLeftLeaves(root.left) if root.left !=None else 0
        summ += self.sumOfLeftLeaves(root.right) if root.right !=None else 0
        return summ
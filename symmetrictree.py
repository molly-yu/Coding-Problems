# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric
# Solution by Molly Yu

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    # First Solution, recursive
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        leftTree = root.left
        rightTree = root.right
        return self.compareTree(leftTree, rightTree)

    def compareTree(self, leftTree, rightTree):
        if leftTree is None and rightTree is None:
            return True
        elif leftTree is None or rightTree is None:
            return False
        if leftTree.val != rightTree.val :
            return False
        else:
            return (self.compareTree(leftTree.left, rightTree.right) and self.compareTree(leftTree.right, rightTree.left))



    
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
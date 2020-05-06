# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Solution by Molly Yu


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # First Solution
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.max_Depth(root, 1)

    def max_Depth(self, root, depth):
        if root.left is None and root.right is None:
            return depth
        elif root.left is None:
            return self.max_Depth(root.right, depth+1)
        elif root.right is None:
            return self.max_Depth(root.left, depth+1)
        return max(self.max_Depth(root.left, depth +1), self.max_Depth(root.right, depth+1))

    # Cleaned up code (slightly slower run time) but less robust
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.max_Depth2(root, 0)

    def max_Depth2(self, root, depth):
        if root is None:
            return depth
        return max(self.max_Depth2(root.left, depth +1), self.max_Depth2(root.right, depth+1))

    # Similar solution, more consise and without using helper, adding 1 each time
    def maxDepth3(self, root):
     return 1 + max(self.maxDepth3(root.left), self.maxDepth3(root.right)) if root else 0


     # Iterative Solution to be added
        
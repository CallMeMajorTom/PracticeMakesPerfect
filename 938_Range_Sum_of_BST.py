#Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
#
#The binary search tree is guaranteed to have unique values.
#
#Example 1:
#
#Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
#Output: 32
#Example 2:
#
#Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
#Output: 23
#
#Note:
#
#The number of nodes in the tree is at most 10000.
#The final answer is guaranteed to be less than 2^31.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#384 ms
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        s = 0
        if root.val < L:
            s = s + self.rangeSumBST(root.right,L,R)
        elif root.val > R:
            s = s + self.rangeSumBST(root.left,L,R)
        else:
            s = s + root.val
            s = s + self.rangeSumBST(root.right,L,R)
            s = s + self.rangeSumBST(root.left,L,R)

        return s

#244ms
class Solution:
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0

        s = 0

        if root.val >= L:
            s += self.rangeSumBST(root.left, L, R)

        if root.val <= R:
            s += self.rangeSumBST(root.right, L, R)

        if L <= root.val <= R:
            s += root.val

        return s

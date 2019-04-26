#We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
#
#Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
#
#(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
#
#Example 1:
#Input: [1,null,0,0,1]
#Output: [1,null,0,null,1]
#
#Explanation:
#Only the red nodes satisfy the property "every subtree not containing a 1".
#The diagram on the right represents the answer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumSubtree(self,root):
        s = root.val
        if root.right:
            s = s + self.sumSubtree(root.right)
        if root.left:
            s = s + self.sumSubtree(root.left)

        return s

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.sumSubtree(root) == 0:
                root = None
        else:
            if root.left:
                root.left = self.pruneTree(root.left)
            if root.right:
                root.right = self.pruneTree(root.right)

        return root

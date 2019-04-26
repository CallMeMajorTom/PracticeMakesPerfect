## Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
##
## You should preserve the original relative order of the nodes in each of the two partitions.
##
## Example:
##
## Input: head = 1->4->3->2->5->2, x = 3
## Output: 1->2->2->4->3->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 遍历head链表，将小于x的加入smallHead链表，大于等于x的加入bigHead链表，然后合并两个链表
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallHead = ListNode(-1)
        bigHead = ListNode (-1)
        smallptr = smallHead
        bigptr = bigHead
        while head:
            if head.val < x:
                smallptr.next = head
                smallptr = smallptr.next
            else:
                bigptr.next = head
                bigptr = bigptr.next
            head = head.next
        smallptr.next = bigHead.next
        bigptr.next = None
        return smallHead.next

## Write a program to find the node at which the intersection of two singly linked lists begins.
##
## For example, the following two linked lists:
##
## A: a1,a2,c1,c2,c3
## B: b1,b2,b3,c1,c2,c3
##
## begin to intersect at node c1.

# 求两个链表的交点，先使两链表对齐（长度一致）
# A: a1,a2,c1,c2,c3
# B: b2,b3,c1,c2,c3
# 两个链表的头指针一起向后移动，遇到相等的返回

class Solution(object):
    def _getLinkLen(self,head):
        Len = 0
        while head:
            head = head.next
            Len = Len + 1
        return Len

    def getIntersectionNode(self,headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self._getLinkLen(headA)
        lenB = self._getLinkLen(headB)
        if lenB > lenA:
            while lenB > lenA:
                headB = headB.next
                lenB = lenB - 1
        else:
            while lenA > lenB:
                headA = headA.next
                lenA = lenA - 1
        while headA:
            if headA ==  headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

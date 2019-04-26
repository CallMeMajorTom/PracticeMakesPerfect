## Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
##
## Example:
##
## Input:
## [
##   1->4->5,
##   1->3->4,
##   2->6
## ]
## Output: 1->1->2->3->4->4->5->6

# 思路：分治
# l1,l2,l3,l4,l5 (合并l1,l2，合并l3,l4)
# l1,   l3,   l5（合并l1,l3）
# l1,         l5（合并l1,l5）
# l1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not len(lists):
            return None
        total = len(lists)
        interval = 1
        while interval < total:
            for i in range(0,total - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval = interval * 2
        return lists[0]

    def mergeTwoLists(self, l1, l2): ## 21题相同
        head = ListNode(0)
        ptr = head
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        return head.next


#思路：递归
# l1,l2 || l3,l4,l5 (分为[l1,l2]和[l3,l4,l5])
# l1,l2 || l3,l4,l5（合并l1,l2，将[l3,l4,l5]分为[l3]和[l4,l5]）
# l1    || l3 | l4,l5 (合并l4，l5)
# l1    || l3 | l4 (合并l3,l4)
# l1    || l3 （合并l1,l3）
# l1

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not len(lists):
            return None
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0],lists[1])
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)/2
        sublist1 = []
        sublist2 = []
        for i in range(mid):
            sublist1.append(lists[i])
        for i in range(mid,len(lists)):
            sublist2.append(lists[i])
        l1 = self.mergeKLists(sublist1)
        l2 = self.mergeKLists(sublist2)
        return self.mergeTwoLists(l1,l2)

    def mergeTwoLists(self, l1, l2): ## 21题相同
        head = ListNode(0)
        ptr = head
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        return head.next

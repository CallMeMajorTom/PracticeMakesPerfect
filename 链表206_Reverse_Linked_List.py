## Reverse a singly linked list.
##
## Example:
##
## Input: 1->2->3->4->5->NULL
## Output: 5->4->3->2->1->NULL
## Follow up:
##
## A linked list can be reversed either iteratively or recursively. Could you implement both?


# 思路一(iteratively)：
# 新链表初始为0，遍历旧链表，依次加到新链表的表头（使遍历到的节点next指向新链表）

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        while(head):
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode
        return newHead

# 思路二(recursively)：
# step0 A: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø B: Ø
# step1 A: n2 → … → nk-1 → nk → nk+1 → … → nm → Ø B: Ø ← n1
# stepN A: n3 → … → nk-1 → nk → nk+1 → … → nm → Ø B: Ø ← n1 ← n2
# Final A: Ø B: Ø ← n1 ← n2 ← … ← nm

class Solution(object):
    def _reverseList(self,head,newHead):
        if not head:
            return newHead
        nextNode = head.next
        head.next = newHead
        return self._reverseList(nextNode, head)

    def reverseList(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverseList(head, None)

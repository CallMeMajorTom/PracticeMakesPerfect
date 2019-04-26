## Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
## To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
##
## Note: Do not modify the linked list.
##
## Example 1:
##
## Input: head = [3,2,0,-4], pos = 1
## Output: tail connects to node index 1
## Explanation: There is a cycle in the linked list, where tail connects to the second node.

# 快慢指针法，o(n)，详见 链表142_Linked_List_Cycle_II.png
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #快慢指针
        fast = head
        slow = head
        meet = None
        while slow and fast:
            slow = slow.next #先各自走一步
            fast = fast.next
            if not fast:
                return None #如果遇到链表尾，说明无环
            fast = fast.next #未遇到链表尾，快指针再走
            if slow == fast: #如果快慢指针相遇，标记
                meet = fast
                break

        while meet and not meet == head: #从meet处和head处同时出发，相遇处为环头
            meet = meet.next
            head = head.next
        return meet

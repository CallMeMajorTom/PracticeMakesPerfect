## Reverse a linked list from position m to n. Do it in one-pass.
##
## Note: 1 ≤ m ≤ n ≤ length of list.
##
## Example:
##
## Input: 1->2->3->4->5->NULL, m = 2, n = 4
## Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：
# 找到需要逆序的开头及其前置节点，逆序m至n段链表， 链接前置节点至新的开头，逆序后的结尾连接到原有的后置节点

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        changeLen = n - m + 2
        result = head
        pre = None
        while head and m-1:
            pre = head
            head = head.next
            m = m - 1

        newHead = None
        newTail = head

        while head and changeLen - 1:
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode
            changeLen = changeLen - 1
        newTail.next = head
        if pre:
            pre.next = newHead
        else:
            return newHead

        return result

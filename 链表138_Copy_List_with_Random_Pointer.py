## 深拷贝
## A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
##
## Return a deep copy of the list.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        location = dict()

        #创建字典，键是Node，值是原链表中位置
        ptr = head
        loc = 0
        while ptr:
            location[ptr] = loc
            loc = loc + 1
            ptr = ptr.next


        #创建一个原链表顺序的新List，List中的Node值与原序列相同，random和next指针置空
        ptr = head
        newLink = []
        while ptr:
            newLink.append(Node(ptr.val,None,None))
            ptr = ptr.next

        #给新List中所有Node的random和next指针赋值，从字典中读取其位置之后在list中找到该节点
        ptr = head
        while ptr:
            if not location.get(ptr.random, -1) == -1: #dict.get(“WhatYouWant”, default)如果字典中无法找到“WhatYouWant”，返回default
                newLink[location[ptr]].random = newLink[location.get(ptr.random)]
            else:
                newLink[location[ptr]].random = None
            if not location.get(ptr.next, -1) == -1:
                newLink[location[ptr]].next =  newLink[location.get(ptr.next)]
            else:
                newLink[location[ptr]].next = None
            ptr = ptr.next

        if len(newLink) >= 1:
            return newLink[0]
        else:
            return None

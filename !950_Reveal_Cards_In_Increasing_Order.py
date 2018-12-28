#In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.
#
#Initially, all the cards start face down (unrevealed) in one deck.
#
#Now, you do the following steps repeatedly, until all cards are revealed:
#
#Take the top card of the deck, reveal it, and take it out of the deck.
#If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
#If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
#Return an ordering of the deck that would reveal the cards in increasing order.
#
#The first entry in the answer is considered to be the top of the deck.
#
#
#
#Example 1:
#
#Input: [17,13,11,2,3,5,7]
#Output: [2,13,3,11,5,17,7]
#Explanation:
#We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
#After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
#We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
#We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
#We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
#We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
#We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
#We reveal 13, and move 17 to the bottom.  The deck is now [17].
#We reveal 17.
#Since all the cards revealed are in increasing order, the answer is correct.
#
#
#Note:
#
#1 <= A.length <= 1000
#1 <= A[i] <= 10^6
#A[i] != A[j] for all i != j

#简化描述
#给定一个序列，经过一个操作算法，变为另一个序列，已知操作算法和结果序列，求原序列。

#解题思路1：
#模拟（Simulation）
#初始化队列queue存储递增序号[0, 1, 2, ..., len(deck) - 1]
#将输入的扑克deck从小到大排序
#利用映射字典dict存储序号与扑克之间的映射关系
#用queue模拟翻牌过程，记队列头部元素为t
#第一步令dic[t] = deck.pop(0)
#第二步将t加入queue的尾部
#重复执行如上过程，直到queue为空。
#将字典按照key排序，输出value即为答案

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        queue = list(range(len(deck)))
        dict = {}
        while 1:
            dict[queue.pop(0)] = deck.pop(0)    #第一步
            if not queue:
                break
            queue.append(queue.pop(0))  #第二步
        for key in sorted(dict.keys()):
            queue.append(dict[key])

        return queue

#解题思路2：
#模拟（Simulation）逆向过程
#初始为一个空队列
#第一步尾部元素加入队列的头部
#第二步在头部加入当前最大元素

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        d = collections.deque()
        for x in sorted(deck)[::-1]:
            d.rotate() #第一步
            d.appendleft(x) #第二步
        return list(d)

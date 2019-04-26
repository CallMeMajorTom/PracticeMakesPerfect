## Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
##
##
##
## Example 1:
##
## Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
## Output: true
## Explanation: We might do the following sequence:
## push(1), push(2), push(3), push(4), pop() -> 4,
## push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
## Example 2:
##
## Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
## Output: false
## Explanation: 1 cannot be popped before 2.

# 队列：[4,5,3,2,1]，等待入栈：[1,2,3,4,5]
# step1:1,2,3入栈
# step2:4入栈，栈顶（4）与当前队头（4）相同，4出队，4出栈，说明截止目前队列可行
# step3:5入栈，栈顶（5）与当前队头（5）相同，5出队，5出栈，说明截止目前队列可行
# step4:栈顶（3）与当前队头（3）相同，3出队，3出栈，说明截止目前队列可行
# step5:栈顶（2）与当前队头（2）相同，2出队，2出栈，说明截止目前队列可行
# step6:栈顶（1）与当前队头（1）相同，1出队，1出栈，说明截止目前队列可行
# 队空，该方案可行

# 队列：[4,3,5,1,2]，等待入栈：[1,2,3,4,5]
# step1:1,2,3入栈
# step2:4入栈，栈顶（4）与当前队头（4）相同，4出队，4出栈，说明截止目前队列可行
# step3:栈顶（3）与当前队头（3）相同，3出队，3出栈，说明截止目前队列可行
# step4:5入栈，栈顶（5）与当前队头（5）相同，5出队，5出栈，说明截止目前队列可行
# step5:栈顶（2）与当前对头（1）不相同，同时此时所有元素已经入栈，说明此队列不可行（目前栈内【2，1】，不可以【1，2】顺序出栈）

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # 使用栈和队列
        # 队列存储popped，栈按照pushed顺序入栈
        # popped队列的对头，应当在某一个入栈时刻是栈顶

        self._pushedS = collections.deque()
        self._poppedQ = collections.deque()

        for p in pushed:
            self._pushedS.appendleft(p)
            while len(self._pushedS) and len(popped) and self._pushedS[0] == popped[0]:
                popped = popped[1:]
                self._pushedS.popleft()

        if len(popped) >= 1:
            return False
        else:
            return True

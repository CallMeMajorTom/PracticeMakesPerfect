## Implement the following operations of a stack using queues.
##
## push(x) -- Push element x onto stack.
## pop() -- Removes the element on top of the stack.
## top() -- Get the top element.
## empty() -- Return whether the stack is empty.
## Example:
##
## MyStack stack = new MyStack();
##
## stack.push(1);
## stack.push(2);
## stack.top();   // returns 2
## stack.pop();   // returns 2
## stack.empty(); // returns false

# 思路：
# 栈与队列的区别：后进先出与先进先出，因此只要使用队列设计栈的push操作，使元素顺序正确，出栈操作直接使用出队操作即可。
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()
        ## 示例，用法
        ## >>> from collections import deque
        ## >>> q = deque(['a', 'b', 'c'])
        ## >>> q.append('x')
        ## >>> q.appendleft('y')
        ## >>> q
        ## deque(['y', 'a', 'b', 'c', 'x'])
        ## deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # 使用一个临时队列，将新元素插入新队列队首，然后依次将旧队列中元素插入
        tmpQ = collections.deque()
        tmpQ.append(x)
        while not self.empty():
            tmpQ.append(self.pop())
        self._queue = tmpQ



    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.empty():
            return self._queue[0]
        else:
            return None


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self._queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

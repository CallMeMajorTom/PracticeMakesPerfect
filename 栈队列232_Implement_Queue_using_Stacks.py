## Implement the following operations of a queue using stacks.
##
## push(x) -- Push element x to the back of queue.
## pop() -- Removes the element from in front of queue.
## peek() -- Get the front element.
## empty() -- Return whether the queue is empty.
## Example:
##
## MyQueue queue = new MyQueue();
##
## queue.push(1);
## queue.push(2);
## queue.peek();  // returns 1
## queue.pop();   // returns 1
## queue.empty(); // returns false

# 思路：
# 栈与队列的区别：后进先出与先进先出，因此只要使用栈设计队列的push操作，使元素顺序正确，出队操作直接使用出栈操作即可。
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = collections.deque()


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        tmpS = collections.deque()
        while not self.empty():
            tmpS.appendleft(self._stack.pop())
        self._stack.appendleft(x)
        while len(tmpS):
            self._stack.appendleft(tmpS.pop())


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._stack.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self._stack[0]
        else:
            return None


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not len(self._stack)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

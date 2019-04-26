## Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
##
## push(x) -- Push element x onto stack.
## pop() -- Removes the element on top of the stack.
## top() -- Get the top element.
## getMin() -- Retrieve the minimum element in the stack.
## Example:
##
## MinStack minStack = new MinStack();
## minStack.push(-2);
## minStack.push(0);
## minStack.push(-3);
## minStack.getMin();   --> Returns -3.
## minStack.pop();
## minStack.top();      --> Returns 0.
## minStack.getMin();   --> Returns -2.

# 思路：设置一个同步栈，该栈保存当前时刻栈最小值，每次push进新值，要进行判断后在同步栈push当前最小值，pop时同步栈也要pop
#     |-5|   |-5|
#     |0 |   |-2|
#     |-2|   |-2|
#     栈     同步栈

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = collections.deque()
        self.minStack = collections.deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._stack.append(x)
        if len(self.minStack) == 0 or x < self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])


    def pop(self):
        """
        :rtype: None
        """
        self.minStack.pop()
        return self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not len(self.minStack) == 0:
            return self.minStack[-1]
        else:
            return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

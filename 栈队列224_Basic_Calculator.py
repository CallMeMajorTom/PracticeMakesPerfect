## Implement a basic calculator to evaluate a simple expression string.
##
## The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
##
## Example 1:
##
## Input: "1 + 1"
## Output: 2
## Example 2:
##
## Input: " 2-1 + 2 "
## Output: 3
## Example 3:
##
## Input: "(1+(4+5+2)-3)+(6+8)"
## Output: 23


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        nStack = collections.deque()
        oStack = collections.deque()
        computeFlag = False
        i = 0
        while i < len(s):
            if s[i].isdigit(): #遇到数字，放入数字栈
                j = i
                while i < len(s) and s[i].isdigit():
                    i = i + 1
                nStack.appendleft(int(s[j : i]))
            elif s[i] == '+':
                #遇到加减，放入符号栈后 1.后面数字，放入数字栈开始后计算 2.后面'('，不计算
                oStack.appendleft(1)
                i = i + 1
                while s[i] == ' ':
                    i = i + 1
                    continue
                if s[i].isdigit():
                    computeFlag = True
                continue
            elif s[i] == '-':
                oStack.appendleft(-1)
                i = i + 1
                while s[i] == ' ':
                    i = i + 1
                    continue
                if s[i].isdigit():
                    computeFlag = True
                continue
            elif s[i] == '(':
                #遇到'('不计算
                computeFlag = False
                i = i + 1
            elif s[i] == ')':
                #遇到')'计算
                computeFlag = True
                i = i + 1
            elif s[i] == ' ':
                #空格
                i = i + 1
            #对栈顶两元素进行计算
            if len(nStack) >= 2 and len(oStack) >= 1 and computeFlag:
                result = nStack.popleft() * oStack.popleft() + nStack.popleft()
                nStack.appendleft(result)

        return nStack.pop()

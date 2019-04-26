#Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
#
#Formally, a parentheses string is valid if and only if:
#
#It is the empty string, or
#It can be written as AB (A concatenated with B), where A and B are valid strings, or
#It can be written as (A), where A is a valid string.
#Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
#
#
#
#Example 1:
#
#Input: "())"
#Output: 1
#Example 2:
#
#Input: "((("
#Output: 3
#Example 3:
#
#Input: "()"
#Output: 0
#Example 4:
#
#Input: "()))(("
#Output: 4

##????????????????并不知道自己在想啥
#Fail on "((())"
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        rightP = [i for i,x in list(enumerate(S)) if x == '(']

        if not rightP or len(rightP) == len(S):
            return len(S)

        count = rightP[0]

        if len(rightP) > 1:
            for i in range(len(rightP)-1):
                if(rightP[i+1] - rightP[i] > 1):
                    count = count + (rightP[i+1] - rightP[i] - 2)
                else:
                    count = count + 1
            if rightP[i+1] == len(S)-1:
                count = count + 1

        else:
            if(rightP[0] < len(S)-1):
                count = count + (len(S) - rightP[0] - 2)
            else:
                count = count + 1
        return count

#Solution
class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

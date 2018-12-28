#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
#Return the element repeated N times.
#The point is "N+1" "unique" elements =>找到重复元素即可

#Fail
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        setList = list(set(A))
        for item in setList:
            if A.count(item) == len(A)/2 :
                return item

#Brilliant one!
#If a number is repeated N times in a list of size 2N, it is always possible for the repeated number to stay within a distance of 2.
#Consider this exaple where N = 4, Number x is repeated twice. All possible comibnations for x to fit in a list of size 4 are:
#[a,b,x,x]
#[x,a,b,x] (distance between both the x is still 1, consider it as a circular list, -1 in python's list means last one)
#[x,a,x,b]
#[x,x,a,b]
#[a,x,b,x]
#[a,x,x,b]
class Solution:
    def repeatedNTimes(self, A):
        for i in range(len(A)):
            if A[i - 1] == A[i] or A[i - 2] == A[i]:
                return A[i]

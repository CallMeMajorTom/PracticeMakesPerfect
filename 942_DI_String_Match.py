#Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
#Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
#If S[i] == "I", then A[i] < A[i+1]
#If S[i] == "D", then A[i] > A[i+1]
#
#
#Example 1:
#
#Input: "IDID"
#Output: [0,4,1,3,2]
#Example 2:
#
#Input: "III"
#Output: [0,1,2,3]
#Example 3:
#
#Input: "DDI"
#Output: [3,2,0,1]


#愚蠢思路：
#根据I和D的趋势判断各位置上的数字应该在哪一层级
#从高层级开始蛇形向下赋值
#如“DDI”=》层级【0，-1，-2，-1】
#赋值过程是
#0层：list[0] = 3
#-1层：list[3] = 2，list[1] = 1
#-2层：list[2] = 0
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        layer = [0]
        list = range(len(S)+1)
        for i in range(len(S)):
            if S[i] == 'I':
                layer.append(layer[i]+1)
            else:
                layer.append(layer[i]-1)
        layerMax = max(layer)
        layerMin = min(layer)
        count = len(S)
        for j in range(layerMax,layerMin-1,-1):
            indexs = []
            indexs = [i for i,x in enumerate(layer) if x==j]
            if(j % 2 == 1):
                for index in indexs:
                    list[index] = count
                    count = count - 1
            else:
                for index in indexs[::-1]:
                    list[index] = count
                    count = count - 1
        return list

#神仙思路：
#第一个为I的情况下，第一个数永远是最小值（初始为0）；反之则永远是最大值
#对于除了第一个元素外的序列list[1:]，上面的规则同样适用，所以算法思路是追踪最大最小值，顺序赋值
#如：如“DDI"
#DDI序列=》元素为最大值3，DI序列=》元素为当前最大值2，I序列=》元素为当前最小值0

class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]

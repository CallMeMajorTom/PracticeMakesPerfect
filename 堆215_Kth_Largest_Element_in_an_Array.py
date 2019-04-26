## Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
##
## Example 1:
##
## Input: [3,2,1,5,6,4] and k = 2
## Output: 5
## Example 2:
##
## Input: [3,2,3,1,2,4,5,5,6] and k = 4
## Output: 4
## Note:
## You may assume k is always valid, 1 ≤ k ≤ array's length.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 维护一个规模为k的最小堆（heap会重新把内部的数据进行整合，heap的顶端永远是最小的值）
        # 遍历nums，如果元素比最小堆堆顶大，就pop堆顶，插入元素。
        from heapq import *
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for n in nums[k:]:
            if n > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,n)
        return min_heap[0]

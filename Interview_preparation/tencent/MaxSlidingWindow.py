#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 17:10
# @File    : MaxSlidingWindow.py
from typing import List

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        构建大顶堆
        :param nums:
        :param k:
        :return:
        """
        # 先对前k个数据构建大顶堆
        head = [(nums[i], i) for i in range(k)]
        self.topKHeap(head)

        # 保存滑动窗口最大值
        ans = [head[0][0]]
        for j in range(k, len(nums)):
            head.append((nums[j], j))
            while head[0][1] <= (j - k):
                head.pop(0)
                self.topKHeap(head)

            self.topKHeap(head)
            ans.append(head[0][0])
        return ans

    def topKHeap(self, head):
        k = len(head)
        for i in range(k // 2 - 1, -1, -1):
            self.build_head(head, i, k - 1)

    def build_head(self, head, i, n):
        """
        构建大顶堆
        :param head:
        :param i:
        :param n:
        :return:
        """
        left, right = 2 * i + 1, 2 * i + 2

        max_index = i
        if left <= n and head[left][0] > head[max_index][0]:
            max_index = left

        if right <= n and head[right][0] > head[max_index][0]:
            max_index = right

        if max_index != i:
            head[max_index], head[i] = head[i], head[max_index]
            return self.build_head(head, max_index, n)


if __name__ == '__main__':
    print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

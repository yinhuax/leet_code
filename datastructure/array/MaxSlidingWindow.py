#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/28 22:14
# @File    : MaxSlidingWindow.py
from typing import List

"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

"""


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        维护大小为k的双端队列
        :param nums:
        :param k:
        :return:
        """
        from collections import deque
        if not nums or k == 0: return []
        deque = deque()
        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])

        res = [deque[0]]
        for i in range(k, len(nums)):  # 形成窗口后
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

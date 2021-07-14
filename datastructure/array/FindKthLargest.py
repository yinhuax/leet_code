#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 19:12
# @File    : FindKthLargest.py
from typing import List

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""


class FindKthLargest(object):

    def __init__(self):
        pass

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
        :param nums:
        :param k:
        :return:
        """
        # 构建小顶堆
        n = len(nums)
        head = nums[:k]

        for i in range(k // 2 - 1, -1, -1):
            # 从第一个非叶子节点开始构建小顶堆
            self.build_head(i, k - 1, head)

        # 若K之后的元素大于根节点，该元素与堆顶元素交换，然后重新调整小顶堆
        for j in range(k, n):
            if nums[j] > head[0]:
                head[0] = nums[j]
                # 重新调整小顶堆
                self.build_head(0, k - 1, head)

        return head[0]

    def build_head(self, i, n, nums):
        """
        小顶堆构建
        :param i:
        :param n:
        :param nums:
        :return:
        """
        left, right = 2 * i + 1, 2 * i + 2
        min_index = i

        if left <= n and nums[left] < nums[min_index]:
            min_index = left

        if right <= n and nums[right] < nums[min_index]:
            min_index = right

        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]
            self.build_head(min_index, n, nums)

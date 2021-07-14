#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 16:36
# @File    : Heap_sort.py
"""
堆排序实现
"""
from typing import List


class Heap_sort(object):

    def __init__(self):
        pass

    def build_head(self, i, j, nums: List[int]):
        """
        构建大顶堆
        :param i:
        :param j:
        :param nums:
        :return:
        """
        # 左右叶子节点的下标
        left, right = 2 * i + 1, 2 * i + 2
        large_index = i
        # 与左节点比较
        if left <= j and nums[i] < nums[left]:
            large_index = left

        if right <= j and nums[right] > nums[large_index]:
            large_index = right

        # 从三个节点中得到较大元素的下标，如果较大下标不是父结点下标，说明交互后需要重新调整大顶堆
        if large_index != i:
            nums[i], nums[large_index] = nums[large_index], nums[i]
            self.build_head(large_index, j, nums)

    def heap_sort(self, nums):
        """
        堆排序
        :param nums:
        :return:
        """
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            # 构造大顶堆，从非叶子节点开始倒序遍历，因此n // 2 - 1就是最后一个叶子节点
            self.build_head(i, n - 1, nums)

        print(nums)

        # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆
        for j in range(n - 1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.build_head(0, j - 1, nums)

        return nums


if __name__ == '__main__':
    print(Heap_sort().heap_sort([1, 3, 7, 6, 5, 9, 8]))

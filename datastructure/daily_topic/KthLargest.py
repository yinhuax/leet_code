#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 9:47
# @File    : KthLargest.py
from typing import List

"""

设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
 
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        if len(nums) >= self.k:
            self.heap_create()
        else:
            self.heap = []

    def add(self, val: int) -> int:
        # 如果当前元素小于堆顶元素，替换堆顶重新构建小顶堆
        if len(self.heap) < self.k:
            self.nums.append(val)
            # 让其有序化
            self.heap_create()
        elif self.heap and val > self.heap[0]:
            self.heap[0] = val
            self.build_heap(0, self.k - 1, self.heap)

        return self.heap[0]

    def build_heap(self, i, n, nums):
        left, right = 2 * i + 1, 2 * i + 2
        min_index = i

        if left <= n and nums[left] < nums[min_index]:
            min_index = left

        if right <= n and nums[right] < nums[min_index]:
            min_index = right

        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]
            self.build_heap(min_index, n, nums)

    def heap_create(self):
        # 构建含K个元素的小顶堆
        self.heap = self.nums[:self.k]
        for i in range(self.k // 2 - 1, -1, -1):
            self.build_heap(i, self.k - 1, self.heap)

        # 如果后面元素小于堆尾元素
        for j in range(self.k, len(self.nums)):
            # 找到前K大的数
            if self.nums[j] > self.heap[0]:
                self.heap[0] = self.nums[j]
                self.build_heap(0, self.k - 1, self.heap)


if __name__ == '__main__':
    k = KthLargest(2, [0])
    print(k.add(-3))
    print(k.add(-2))
    print(k.add(-4))
    print(k.add(0))
    print(k.add(4))

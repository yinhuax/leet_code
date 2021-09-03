#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/3 16:12
# @File    : SmallestK.py
from typing import List

"""
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：
"""


class HeapSort(object):

    def head_sort(self, arr, k):
        heap = arr[:k]
        for i in range(k // 2, -1, -1):
            self.build_head(heap, i, len(heap) - 1)

        for j in range(k, len(arr)):
            if arr[j] < heap[0]:
                heap[0] = arr[j]
                self.build_head(heap, 0, len(heap) - 1)

        return heap

    def build_head(self, arr, index, n):
        left, right = 2 * index + 1, 2 * index + 2
        max_index = index

        if left <= n and arr[left] > arr[max_index]:
            max_index = left

        if right <= n and arr[right] > arr[max_index]:
            max_index = right

        if max_index != index:
            arr[max_index], arr[index] = arr[index], arr[max_index]
            return self.build_head(arr, max_index, n)


class MaxHeap(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None] * max_size
        self._count = 0

    def get_length(self):
        return self._count

    def show(self):
        print(self.arr)

    def push(self, value):
        """
        push 使用从底向上的建堆方式
        :param value:
        :return:
        """
        if self._count >= self.max_size:
            raise ValueError("list is full !!!")

        self.arr[self._count] = value
        self._shift_up(self._count)
        self._count += 1

    def _shift_up(self, index):
        if index > 0:
            parent = (index - 1) // 2
            if self.arr[parent] < self.arr[index]:
                # 交换根节点位置
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                self._shift_up(parent)

    def pop(self):
        """
        pop, 输出数组下标为0 的数据，使用尾节点交换到头结点，然后从顶向下构建堆
        :return:
        """
        if self._count < 1:
            raise ValueError("list is empty!!!")

        value = self.arr[0]
        self._count -= 1
        self.arr[0], self.arr[self._count] = self.arr[self._count], self.arr[0]
        self._shift_down(0)
        return value

    def _shift_down(self, index):
        left, right = 2 * index + 1, 2 * index + 2
        max_index = index
        if left < self._count and self.arr[left] > self.arr[max_index]:
            max_index = left

        if right < self._count and self.arr[right] > self.arr[max_index]:
            max_index = right

        if index != max_index:
            self.arr[max_index], self.arr[index] = self.arr[index], self.arr[max_index]
            self._shift_down(max_index)


class Solution:

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        """
        1、大顶堆实现
        2、排序后取前k个数
        :param arr:
        :param k:
        :return:
        """
        # 堆排
        max_head = MaxHeap(k)
        for i in range(len(arr)):
            if i < k:
                max_head.push(arr[i])
            elif arr[i] < max_head.arr[0]:
                    max_head.pop()
                    max_head.push(arr[i])
        return max_head.arr

    def quick_sort(self, arr: List[int], left, right):
        if left >= right:
            return

        # 设置right为 哨兵
        x = arr[right]
        i = left
        j = right
        while i < j:
            while i < j and arr[i] <= x:
                i += 1
            while i < j and arr[j] > x:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                # 特殊情况处理
                if arr[i] == arr[j] == arr[x]:
                    i += 1
                    j -= 1

        # arr[right], arr[j] = arr[j], arr[right]
        self.quick_sort(arr, left, j - 1)
        self.quick_sort(arr, j, right)

    def merge_sort(self, arr, left, right):
        if left >= right:
            return

        mid = left + right >> 1
        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid + 1, right)
        self.merge(arr, left, right, mid)

    def merge(self, arr, left, right, mid):
        """
        使用额外空间，合并有序数组
        :param arr:
        :param left:
        :param right:
        :param mid:
        :return:
        """
        i = left
        j = mid + 1
        temp = []
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        temp.extend(arr[i: mid + 1])
        temp.extend(arr[j: right + 1])
        arr[left:right + 1] = temp


if __name__ == '__main__':
    print(Solution().smallestK(arr=[1, 2, 3], k=0))

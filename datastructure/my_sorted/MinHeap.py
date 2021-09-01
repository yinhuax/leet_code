#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/1 16:34
# @File    : MinHeap.py

import numpy as np
# 手写最小堆实现
class MaxHeap(object):

    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.li = [None] * maxSize
        self.count = 0

    def length(self):
        # 求数组的长度
        return self.count

    def show(self):
        if self.count <= 0:
            print("null")
        else:
            print(self.li[:self.count])

    def push(self, value):
        if self.count >= self.maxSize:  # 判断是否数组越界
            raise Exception("full")

        self.li[self.count] = value  # 将新节点增加到最后
        self._shift_up(self.count)  # 递归构建大顶堆
        self.count += 1

    def _shift_up(self, index):
        # 往大顶堆中添加元素，并保证根节点是最大值:
        # 1. 增加新的值到最后一个节点
        # 2. 与父节点比较，如果比父节点值大，则交换
        if index > 0:
            parent = (index - 1) // 2  # 找到根节点
            # 交换节点
            if self.li[index] > self.li[parent]:
                self.li[parent], self.li[index] = self.li[index], self.li[parent]
                # 继续递归从底网上判断
                self._shift_up(parent)

    def pop(self):
        # 弹出堆顶节点
        # 1. 删除根节点，将最后一个节点作为根节点
        # 2. 判断根节点与左右节点的大小，交换左右节点较大的
        if not self.count:
            raise Exception("null")

        value = self.li[0]
        self.count -= 1
        self.li[0] = self.li[self.count]  # 将最后一个值变为第一个
        self._shift_down(0)
        return value

    def _shift_down(self, index):
        left, right = 2 * index + 1, 2 * index + 2

        max_index = index
        if left < self.length() and self.li[left] > self.li[max_index]:
            max_index = left

        if right < self.length() and self.li[right] > self.li[max_index]:
            max_index = right

        if max_index != index:
            self.li[max_index], self.li[index] = self.li[index], self.li[max_index]
            return self._shift_down(max_index)

class MinHeap(object):

    def __init__(self, maxSize=10):
        self.maxSize = maxSize
        self.arr = [None] * self.maxSize
        self._count = 0

    def get_length(self):
        return self._count

    def show(self):
        if self._count <= 0:
            raise ValueError("Null")

        print(self.arr[:self._count], end=', ')

    def push(self, value):
        # 增加元素
        if self._count >= self.maxSize:
            raise Exception("The array is full!!!")

        self.arr[self._count] = value
        self._shift_up(self._count)
        self._count += 1

    def _shift_up(self, index):
        # 添加新元素到数组末尾，然后从底往上交换数据，与根节点比较，比根节点小就交换
        if index > 0:
            parent = (index - 1) // 2
            if self.arr[parent] > self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                self._shift_up(parent)

    def pop(self):
        # pop堆顶，并更新数组
        if self._count <= 0:
            raise Exception("The array is Empty!!!")

        value = self.arr[0]
        self._count -= 1
        # 将最后一个节点放到前面
        self.arr[0] = self.arr[self._count]
        self._shift_down(0)

        return value

    def _shift_down(self, index):
        n = self.get_length()
        left, right = 2 * index + 1, 2 * index + 2
        min_index = index

        if left < n and self.arr[left] < self.arr[min_index]:
            min_index = left

        if right < n and self.arr[right] < self.arr[min_index]:
            min_index = right

        if min_index != index:
            self.arr[min_index], self.arr[index] = self.arr[index], self.arr[min_index]
            return self._shift_down(min_index)


if __name__ == '__main__':
    m = MinHeap(10)
    np.random.seed(123)

    num = np.random.randint(100, size=10)

    for i in num:
        m.push(i)

    m.show()

    for i in range(5):
        print(m.pop(), end=",")

    m.show()

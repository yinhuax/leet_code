#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/1 11:35
# @File    : MaxHeap.py

# 最大堆实现
import numpy as np
import pandas as pd


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


if __name__ == '__main__':
    m = MaxHeap(10)
    np.random.seed(123)

    num = np.random.randint(100, size=10)

    for i in num:
        m.push(i)

    m.show()

    for i in range(5):
        print(m.pop(), end=",")

    m.show()

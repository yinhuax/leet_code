#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/17 21:54
# @File    : MyCircularQueue.py


class MyCircularQueue(object):

    def __init__(self, k):
        self.k = k
        self.p_start = -1
        self.p_end = -1
        self.data = []

    def enQueue(self, x: int) -> bool:
        # 如果队列没有满，可以插入队列
        if self.isFull():
            return False

        if self.isEmpty():
            self.p_start = 0

        self.p_end = (self.p_end + 1) % self.k
        self.data.insert(self.p_end, x)
        return True

    def deQueue(self) -> bool:
        # 如果队列为空，返回-1
        if self.isEmpty():
            return False

        if self.p_start == self.p_end:
            # 删除到最后一个元素
            self.p_start = self.p_end = -1
            return True

        self.p_start = (self.p_start + 1) % self.k
        return True

    def isFull(self):
        return (self.p_end + 1) % self.k == self.p_start

    def isEmpty(self):
        return self.p_start == -1

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.p_start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.p_end]


if __name__ == '__main__':
    pass

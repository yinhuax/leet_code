#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/17 21:29
# @File    : MyQueue.py

class MyQueue(object):

    def __init__(self):
        self.p_start = 0
        self.data = []

    def enQueue(self, x: int) -> bool:
        self.data.append(x)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.p_start += 1
        return True

    def isEmpty(self) -> bool:
        return self.p_start >= len(self.data)

    def getFront(self):
        return self.data[self.p_start]


if __name__ == '__main__':
    q = MyQueue()
    q.enQueue(5)
    q.enQueue(3)
    q.enQueue(4)

    print(q.getFront())
    print(q.deQueue())
    print(q.getFront())

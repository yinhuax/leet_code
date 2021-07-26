#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/26 14:53
# @File    : LinkedListByList.py

"""
使用数组实现链表
"""


class LinkedListByList(object):

    def __init__(self):
        self.linked_data = [0] * 100010
        self.linked_ne = [0] * 100010
        self.idx = 0
        self.head = -1

    def insert(self, k, x):
        k = k - 1
        self.linked_data[self.idx] = x
        self.linked_ne[self.idx] = self.linked_ne[k]
        self.linked_ne[k] = self.idx
        self.idx += 1

    def addHead(self, x):
        self.linked_data[self.idx] = x
        self.linked_ne[self.idx] = self.head
        self.head = self.idx
        self.idx += 1

    def remove(self, k):
        k = k - 1
        self.linked_ne[k] = self.linked_ne[self.linked_ne[k]]


if __name__ == '__main__':
    linked = LinkedListByList()
    linked.addHead(9)
    linked.insert(1, 1)
    linked.remove(1)
    linked.remove(0)
    linked.addHead(6)
    linked.insert(3, 6)
    linked.insert(4, 5)
    linked.insert(4, 5)
    linked.insert(3, 4)
    linked.remove(6)

    i = linked.head
    while i != 0:
        print(linked.linked_data[i])
        i = linked.linked_ne[i]

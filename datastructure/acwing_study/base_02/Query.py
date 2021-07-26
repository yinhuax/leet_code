#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/26 13:52
# @File    : Query.py

"""
使用数组模拟队列，普通队列、循环队列
"""


class Query(object):

    def __init__(self):
        self.query_data = [0] * 100000
        self.head = 0  # 队列顶端
        self.top = 0

    def empty(self):
        # 当两个指针相遇时，队列为空
        return self.head >= self.top

    def pop(self):
        self.head += 1
        if self.head == 100000:
            self.head = 0

    def push(self, x):
        self.query_data[self.top] = x
        self.top += 1
        if self.top == 100000:
            self.top = 0

    def query(self):
        # 查询队头元素
        return self.query_data[self.head] if not self.empty() else -1


if __name__ == '__main__':
    query = Query()
    query.push(6)
    print(query.empty())
    print(query.query())
    print(query.pop())
    print(query.empty())
    print(query.push(3))
    print(query.push(4))
    print(query.pop())
    print(query.query())
    print(query.push(6))

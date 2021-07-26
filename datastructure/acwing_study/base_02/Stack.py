#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/26 11:13
# @File    : Stack.py

"""
使用数组模拟栈，包含插入，弹出，取栈顶元素，判断栈是否为空
"""


class Stack(object):

    def __init__(self):
        self.stack = [0] * 100000
        self.stack_top = -1

    def empty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.stack_top == -1

    def push(self, x):
        """
        往栈顶插入一个数x
        :param x:
        :return:
        """
        self.stack_top += 1
        self.stack[self.stack_top] = x

        return True

    def query(self):
        """
        返回栈顶元素，如果栈为空时返回-1
        :return:
        """
        return self.stack[self.stack_top] if not self.empty() else -1

    def pop(self):
        """
        弹出栈顶元素，如果为空弹出-1
        :return:
        """
        top = self.query()
        self.stack_top -= 1

        return top


if __name__ == '__main__':
    stack = Stack()
    print(stack.push(5))
    print(stack.query())
    print(stack.push(6))
    print(stack.pop())
    print(stack.query())
    print(stack.pop())
    print(stack.empty())
    print(stack.push(4))
    print(stack.query())
    print(stack.empty())

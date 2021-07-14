#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/17 22:46
# @File    : BFSDemo.py
from collections import deque


class Node(object):

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BFSDemo(object):

    def __init__(self):
        pass

    def BFS(self, root: Node, target: Node) -> int:
        step = 0
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            step += 1
            for i in range(len(queue)):
                curr = queue.pop()
                if curr is target:
                    return step

                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)

        return -1


if __name__ == '__main__':
    pass

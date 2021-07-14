#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 17:34
# @File    : Connect2.py


class Connect2(object):

    def __init__(self):
        pass

    def connect(self, root: 'Node') -> 'Node':
        """
        使用从左往右遍历方式
        :param root:
        :return:
        """
        pre = root
        while pre:
            tail = head = Node(None)
            cur = pre
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next

            pre = head.next

        return root

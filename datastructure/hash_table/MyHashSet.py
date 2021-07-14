#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/1 13:51
# @File    : MyHashSet.py

"""
python链地址法
"""


class Node(object):

    def __init__(self, val, next):
        self.val = val
        self.next = next


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash_list = [Node(None, None) for _ in range(self.size)]  # 设置初始化表大小为1000

    def add(self, key: int) -> None:
        index = key % self.size
        pre_node = self.hash_list[index]
        cur_node = pre_node.next
        while cur_node:
            if cur_node.val == key:
                break
            pre_node = cur_node
            cur_node = cur_node.next
        else:
            pre_node.next = Node(key, None)

    def remove(self, key: int) -> None:
        index = key % self.size
        pre_node = self.hash_list[index]
        cur_node = pre_node.next
        while cur_node:
            if cur_node.val == key:
                pre_node.next = cur_node.next
                break
            pre_node = cur_node
            cur_node = cur_node.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        pre_node = self.hash_list[index]
        while pre_node:
            if pre_node.val == key:
                return True
            pre_node = pre_node.next

        return False

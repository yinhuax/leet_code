#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 13:53
# @File    : MyHashMap.py


class Node(object):

    def __init__(self, key=None, next=None, value=None):
        """
        链地址法
        """
        self.key = key
        self.next = next
        self.value = value


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash_map = [Node() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        pre_node = self.hash_map[index]
        cur_node = pre_node.next
        while cur_node:
            if cur_node.key == key:
                cur_node.value = value
                break
            pre_node = cur_node
            cur_node = cur_node.next
        else:
            node = Node()
            node.key = key
            node.value = value
            pre_node.next = node

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        pre_node = self.hash_map[index]
        cur_node = pre_node.next
        while cur_node:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        pre_node = self.hash_map[index]
        cur_node = pre_node.next
        while cur_node:
            if cur_node.key == key:
                pre_node.next = cur_node.next
                break
            pre_node = cur_node
            cur_node = cur_node.next

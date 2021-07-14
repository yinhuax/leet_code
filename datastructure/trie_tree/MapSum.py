#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 11:32
# @File    : MapSum.py
"""
实现一个 MapSum 类，支持两个方法，insert 和 sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/trie/x0y426/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

from collections import defaultdict, deque


class TireTree(object):

    def __init__(self):
        self.val = 0
        self.is_word = False
        self.children = defaultdict(TireTree)


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireTree()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for s in key:
            node = node.children[s]
        node.is_word = True
        node.val = val

    def sum(self, prefix: str) -> int:
        # 求和
        sums = 0
        node = self.root
        for s in prefix:
            node = node.children[s]

        # 使用队列继续求和
        queue = deque()
        queue.append(node)
        while queue:
            for _ in range(len(queue)):
                cur_node = queue.pop()
                if cur_node.is_word:
                    sums += cur_node.val

                for child in cur_node.children:
                    queue.append(cur_node.children[child])
        return sums


if __name__ == '__main__':
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    print(map_sum.sum("ap"))
    map_sum.insert("app", 2)
    print(map_sum.sum("ap"))

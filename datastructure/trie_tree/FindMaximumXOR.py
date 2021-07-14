#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 15:21
# @File    : FindMaximumXOR.py
from typing import List
from collections import defaultdict

"""
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/trie/x0floe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TrieTree(object):

    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieTree)


class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        使用前缀树
        :param nums:
        :return:
        """
        root = TrieTree()
        # 将数字转换为二进制并插入到前缀树
        for num in nums:
            cur_node = root
            for i in range(30, -1, -1):
                u = num >> i & 1
                cur_node = cur_node.children[u]

        # 计算与字典树中异或后的最大数
        max_res = 0
        for num in nums:
            cur_node = root
            res = 0
            for i in range(30, -1, -1):
                u = num >> i & 1
                # 优先走二进制取反路径
                if (1 ^ u) in cur_node.children:
                    res += 1 << i
                    cur_node = cur_node.children[1 ^ u]
                else:
                    cur_node = cur_node.children[u]
            max_res = max(max_res, res)

        return max_res


if __name__ == '__main__':
    print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))

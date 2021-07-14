#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 22:16
# @File    : FirstUniqChar.py

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/hash-table/xxx94s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class FirstUniqChar(object):

    def __init__(self):
        pass

    def firstUniqChar(self, s: str) -> int:
        """
        使用哈希表，计数排序法
        :param s:
        :return:
        """
        hash_table = dict()

        for i in range(len(s)):
            if s[i] in hash_table:
                hash_table[s[i]] += i
                continue

            hash_table[s[i]] = 0

        for i in range(len(s)):
            if hash_table[s[i]] == 0:
                return i

        return -1

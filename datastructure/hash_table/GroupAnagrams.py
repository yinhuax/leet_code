#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/3 23:22
# @File    : GroupAnagrams.py
from typing import List


class GroupAnagrams(object):

    def __init__(self):
        pass

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        使用hash表
        :param strs:
        :return:
        """
        from collections import defaultdict
        hash_table = defaultdict(list)
        # 去掉重复, 插入哈希表时不需要判断
        for i in range(len(strs)):
            sort_str = "".join(sorted(strs[i]))
            hash_table[sort_str].append(strs[i])

        return list(hash_table.values())


if __name__ == '__main__':
    print(GroupAnagrams().groupAnagrams(["", ""]))

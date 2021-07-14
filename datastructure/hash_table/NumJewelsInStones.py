#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/4 22:46
# @File    : NumJewelsInStones.py

"""
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/hash-table/xx2a0c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class NumJewelsInStones(object):

    def __init__(self):
        pass

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = set(jewels)

        result = 0
        for i in range(len(stones)):
            if stones[i] in seen:
                result += 1
        return result

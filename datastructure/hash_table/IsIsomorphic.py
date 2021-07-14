#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 21:27
# @File    : IsIsomorphic.py
"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/hash-table/xhjvbj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class IsIsomorphic(object):

    def __init__(self):
        pass

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        哈希表写法
        :param s:
        :param t:
        :return:
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == '__main__':
    print(IsIsomorphic().isIsomorphic(s="foo", t="bar"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/24 22:37
# @File    : StrStr.py

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/cm5e2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class StrStr(object):

    def __init__(self):
        pass

    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP算法，返回子字符串第一个出现的位置
        :param haystack:
        :param needle:
        :return:
        """
        if not needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        # 计算子串的next表
        next_array = self.build_next(needle)
        # 主字符串指针
        n, i = len(haystack), 0
        m, j = len(needle), 0
        while i < n and j < m:
            if j < 0 or haystack[i] == needle[j]:  # 匹配上的情况
                i += 1  # 指针右移
                j += 1
            else:
                # 没有匹配上，主字符串指针不动，模式串根据next_array移动
                j = next_array[j]

        if j == m:
            return i - j
        else:
            return -1

    @staticmethod
    def build_next(needle):
        next_array = [0] * len(needle)
        next_array[0] = -1
        i, j = 1, 0
        while i < len(needle) - 1:
            if j < 0 or needle[i] == needle[j]:
                i += 1
                j += 1
                next_array[i] = j
            else:
                # 回退到上个地方
                j = next_array[j]

        return next_array


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "pi"
    print(StrStr().strStr(haystack=haystack, needle=needle))

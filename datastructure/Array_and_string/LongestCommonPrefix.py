#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/21 23:47
# @File    : LongestCommonPrefix.py
from typing import List


class LongestCommonPrefix(object):

    def __init__(self):
        pass

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        暴力解法：纵向查找，用第一个字符串为基准，依次比较其他字符串相同位置是否相等
        :param strs:
        :return:
        """
        if not strs:
            return ""

        length, counter = len(strs[0]), len(strs)

        for i in range(length):
            s = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != s for j in range(1, counter)):
                return strs[0][:i]

        return strs[0]

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """
        二分查找
        :param strs:
        :return:
        """
        # 最长公共前缀的长度不会超过字符串数组中的最短字符串长度
        if not strs:
            return ""

        def isCommonPrefix1(mid):
            return all(strs[0][:mid] == strs[j][:mid] for j in range(1, len(strs)))

        right = min([len(i) for i in strs])
        left = 0
        while left < right:
            mid = (right - left + 1) // 2 + left  # 偏右
            if isCommonPrefix1(mid):
                left = mid
            else:
                right = mid - 1

        return strs[0][:left]


if __name__ == '__main__':
    print(LongestCommonPrefix().longestCommonPrefix1(["f"]))

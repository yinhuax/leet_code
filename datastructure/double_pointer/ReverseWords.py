#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/30 17:59
# @File    : ReverseWords.py

"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

 

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c8su7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class ReverseWords(object):

    def __init__(self):
        pass

    def reverseWords(self, s: str) -> str:
        """
        翻转字符串
        :param s:
        :return:
        """
        return " ".join([strs[::-1] for strs in s.split(" ") if strs])

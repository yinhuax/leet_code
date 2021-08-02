#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/30 16:57
# @File    : TitleToNumber.py
"""
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
"""


class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        """
        26进制表示
        :param columnTitle:
        :return:
        """
        word_dict = {chr(i + 65): i + 1 for i in range(26)}

        result = 0
        for column in columnTitle:
            result = result * 26 + word_dict[column]
        return result


if __name__ == '__main__':
    print(Solution().titleToNumber("A"))

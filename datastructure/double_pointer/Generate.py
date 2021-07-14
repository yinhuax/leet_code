#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/30 17:11
# @File    : Generate.py
from typing import List

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。
"""


class Generate(object):

    def __init__(self):
        pass

    def generate(self, numRows: int) -> List[List[int]]:
        """
        杨辉三角
        :param numRows:
        :return:
        """
        result = []
        for i in range(numRows):
            result1 = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    value = 1
                else:
                    value = result[i - 1][j - 1] + result[i - 1][j]
                result1.append(value)
            result.append(result1)

        return result


if __name__ == '__main__':
    print(Generate().generate(5))

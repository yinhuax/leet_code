#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/30 17:33
# @File    : GetRow.py
from typing import List

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:"""


class GetRow(object):

    def __init__(self):
        pass

    def getRow(self, rowIndex: int) -> List[int]:
        """
        杨辉三角，空间复杂度O（K），使用一维数组复用
        :param rowIndex:
        :return:
        """
        result = [1] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            for j in range(i, 0, -1):
                if j == 0 or j == i:
                    result[j] = 1
                else:
                    result[j] = result[j - 1] + result[j]

        return result


if __name__ == '__main__':
    print(GetRow().getRow(3))

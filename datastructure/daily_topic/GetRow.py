#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 7:39
# @File    : GetRow.py
from typing import List

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            for j in range(i - 1, 0, -1):
                result[j] = result[j - 1] + result[j]

        return result


if __name__ == '__main__':
    print(Solution().getRow(4))

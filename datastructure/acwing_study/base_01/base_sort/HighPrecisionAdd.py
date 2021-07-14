#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/7 17:40
# @File    : HighPrecisionAdd.py
"""
高精度加法:

实现两个大数相加
"""


class HighPrecisionAdd(object):

    def __init__(self):
        pass

    def add(self, A: str, B: str):
        """
        高精度加法
        :param A:
        :param B:
        :return:
        """
        if len(A) < len(B):
            return self.add(B, A)

        i = len(A) - 1
        t = 0

        result = []
        while i >= 0 or t > 0:
            # 从后往前遍历
            cur_b = i - (len(A) - 1) + (len(B) - 1)
            if cur_b >= 0:
                t += int(B[cur_b])
            if i >= 0:
                t += int(A[i])
            i -= 1
            result.append(str(t % 10))
            t = t // 10

        return int(''.join(result[::-1]))


if __name__ == '__main__':
    print(HighPrecisionAdd().add("0", "0"))

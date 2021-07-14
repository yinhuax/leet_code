#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/7 17:40
# @File    : HighPrecisionAdd.py
"""
高精度乘法:

实现两个大数相乘
"""


class HighPrecisionDiv(object):

    def __init__(self):
        pass

    def div(self, A: str, B: str):
        """
        两个数字相除，返回商和余数
        :param A:
        :param B:
        :return:
        """
        t = 0
        # 保存商
        result = 0
        # t为余数
        for i in range(len(A)):
            t = t * 10 + int(A[i])
            result = result * 10 + t // int(B)
            t %= int(B)

        return result, t

    def compute_div(self, A: str, B: str):
        """
        高精度乘法
        :param A:
        :param B:
        :return:
        """
        return self.div(A, B)


if __name__ == '__main__':
    print(HighPrecisionDiv().compute_div("7", "3"))

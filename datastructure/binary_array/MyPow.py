#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 13:50
# @File    : MyPow.py

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
"""


class MyPow(object):

    def __init__(self):
        pass

    def myPow(self, x: float, n: int) -> float:
        """
        快速幂算法
        :param x:
        :param n:
        :return:
        """

        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

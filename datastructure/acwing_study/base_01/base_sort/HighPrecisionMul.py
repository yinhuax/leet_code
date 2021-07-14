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


class HighPrecisionMul(object):

    def __init__(self):
        pass

    def mul(self, A: str, B: str):
        """
        两个数字相乘，其中A为大数 大于 B
        :param A:
        :param B:
        :return:
        """
        t = 0
        i = len(A) - 1
        result = []
        while i >= 0 or t > 0:
            # 做乘法运算
            if i >= 0:
                t += int(A[i]) * int(B)
            i -= 1
            result.append(str(t % 10))
            t //= 10

        return int(''.join(result[::-1]))

    def compute_mul(self, A: str, B: str):
        """
        高精度乘法
        :param A:
        :param B:
        :return:
        """
        if self.compare(A, B):
            return self.mul(A, B)
        else:
            return self.mul(B, A)

    def compare(self, A: str, B: str):
        """
        返回A是否大于B
        :param A:
        :param B:
        :return:
        """
        # 数字长度不一致
        if len(A) != len(B):
            return len(A) > len(B)

        # 数字长度一致的情况
        for i in range(len(A)):
            if A[i] != B[i]:
                return int(A[i]) > int(B[i])
        return True


if __name__ == '__main__':
    print(HighPrecisionMul().compute_mul("9", "3"))

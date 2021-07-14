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

    def sub(self, A: str, B: str):
        """
        两个数字相减，其中A 大于 B
        :param A:
        :param B:
        :return:
        """
        t = 0
        i = len(A) - 1
        result = []
        while i >= 0 or t > 0:
            # 从后往前遍历
            cur_b = i - (len(A) - 1) + (len(B) - 1)
            if i >= 0:
                t = int(A[i]) - t
            if cur_b >= 0:
                t = t - int(B[cur_b])

            i -= 1
            result.append(str((t + 10) % 10))
            if t < 0:
                t = 1
            else:
                t = 0

        return int(''.join(result[::-1]))

    def compute_sub(self, A: str, B: str):
        """
        高精度减法，使用大数减小数计算方便很多
        :param A:
        :param B:
        :return:
        """
        if self.compare(A, B):
            return self.sub(A, B)
        else:
            return -self.sub(B, A)


if __name__ == '__main__':
    print(HighPrecisionAdd().compute_sub("999999999999999", "1111111111111111111111111"))

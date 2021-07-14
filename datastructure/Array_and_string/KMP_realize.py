#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/24 21:25
# @File    : KMP_realize.py

"""
KMP 算法，
"""


class KMP(object):

    def __init__(self):
        pass

    def macth(self, P: str, S: str):
        """

        :param P:  子串
        :param S:  需要匹配的字符串
        :return:
        """
        # 构建next数组
        next_array = self.build_array(P)

        # 从左向右
        n = len(P)
        m = len(S)
        i = j = 0
        while i < m and j < n:
            if 0 > j or S[i] == S[j]:
                i += 1
                j += 1
            else:
                # 模式串右移
                j = next_array[j]

        # 返回的是匹配时的位置
        return i - j

    @staticmethod
    def build_array(P):
        """

        :param P:
        :return:
        """
        next_array = [0] * len(P)
        j = next_array[0] = -1

        for i in range(1, len(P)):
            while j >= 0 and (P[i] != P[j + 1]):  # 前后缀不同
                j = next_array[j]  # 向前回溯

            if P[i] == P[j + 1]:
                # 找到相同的前后缀
                j += 1

            next_array[i] = j

        return next_array


if __name__ == '__main__':
    print(KMP().macth("ACTGPACY", "ACTGPACTGKACTGPACY"))

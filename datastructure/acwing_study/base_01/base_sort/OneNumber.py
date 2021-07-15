#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/15 7:30
# @File    : OneNumber.py

"""
返回数列中每个数对应二进制表示中1的个数
"""


class OneNumber(object):

    def __init__(self):
        pass

    def lowbit(self, num):
        """
        返回最后一个1
        :param num:
        :return:
        """
        return num & -num

    def number(self, nums):
        """
        求数列中每个数的二进制表示中1的个数

        :param nums:
        :return:
        """
        # TODO:  先了解原码、补码、反码，举例
        #        原码： 1010
        #        反码:  0101
        #        补码:  0110  补码=反码 + 1        -x = ~x + 1
        #           x & -x = 0010 获得最末尾出现1的位置
        result = []
        for num in nums:
            count = 0
            while num:
                num -= self.lowbit(num)
                count += 1

            result.append(count)
        return result


if __name__ == '__main__':
    print(OneNumber().number([1, 2, 3, 4, 5]))

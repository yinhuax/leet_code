#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/29 17:33
# @File    : FindNthDigit.py
"""
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。

 

注意：n 是正数且在 32 位整数范围内（n < 231）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-digit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def findNthDigit(self, n: int) -> int:
        """
        找到第n位数字，动态规划？ 二分查找？   怎么生成n个数字
        :param n:
        :return:
        """
        if n < 10:
            return n

        bit = 1
        bit_count = 9
        while n > (bit * bit_count):
            n -= bit * bit_count
            bit += 1
            bit_count *= 10

        if n % bit == 0:
            return int(str(10 ** (bit - 1) + n // bit - 1)[-1])
        else:
            return int(str(10 ** (bit - 1) + n // bit)[n % bit - 1])


if __name__ == '__main__':
    print(Solution().findNthDigit(9785))

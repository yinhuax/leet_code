#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/29 14:45
# @File    : JudgeSquareSum.py

"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
"""


class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        """
        平方数之和：  二分查找
        :param c:
        :return:
        """
        from math import sqrt

        left = 0
        right = int(sqrt(c)) + 1
        while left <= right:
            result = left ** 2 + right ** 2
            if result == c:
                return True
            elif result < c:
                left += 1
            else:
                right -= 1

        return False


if __name__ == '__main__':
    print(Solution().judgeSquareSum(2))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/30 14:47
# @File    : JudgeSquareSum.py
"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
"""


class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        """
        双指针 + 二分查找，范围为 左指针范围[1, sqrt(c)] 右指针[1, sqrt(c - i ** 2)]
        :param c:
        :return:
        """
        import math

        for i in range(int(math.sqrt(c)) + 1):
            left, right = 0, int(math.sqrt(c - i ** 2)) + 1
            while left < right:
                mid = left + right >> 1
                res = (mid ** 2 + i ** 2)
                if res > c:
                    right = mid - 1
                elif res == c:
                    return True
                else:
                    left = mid + 1
            if 2 * left ** 2 == c:
                return True
        return False

    def judgeSquareSum2(self, c: int) -> bool:
        """
        双指针
        :param c:
        :return:
        """
        import math
        left, right = 0, int(math.sqrt(c)) + 1
        while left < right:
            res = (left ** 2 + right ** 2)
            if res == c:
                return True
            elif res > c:
                right -= 1
            else:
                left += 1

        return 2 * left ** 2 == c


if __name__ == '__main__':
    print(Solution().judgeSquareSum(12389))

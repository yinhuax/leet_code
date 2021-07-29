#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/29 17:13
# @File    : ArrangeCoins.py
"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arranging-coins
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def arrangeCoins(self, n: int) -> int:
        """
        二分，根据小学二年级数学，排列 可知   1 + 2 +... + n = n(n + 1) / 2， 二分范围为0, n / 2 行
        :param n:
        :return:
        """
        left = 0
        right = n // 2 + 1
        while left < right:
            mid = (left + right + 1) >> 1
            result = mid * (mid + 1) // 2
            if result <= n:
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    print(Solution().arrangeCoins(8))

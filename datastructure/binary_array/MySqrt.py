#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 8:31
# @File    : MySqrt.py
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xe9cog/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def mySqrt(self, x: int) -> int:
        """
        平方根
        :param x:
        :return:
        """
        left = 0
        right = x
        while left < right:
            mid = (right - left + 1) // 2 + left
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid

        return left


if __name__ == '__main__':
    print(Solution().mySqrt(8))

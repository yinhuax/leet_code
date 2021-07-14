#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 14:07
# @File    : IsPerfectSquare.py
"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xel3tc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        """
        二分查找
        :param num:
        :return:
        """
        left, right = 0, num

        while left <= right:
            mid = (right - left) // 2 + left
            res = mid ** 2
            if res == num:
                return True
            elif res > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == '__main__':
    print(Solution().isPerfectSquare(14))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/24 8:25
# @File    : Find132pattern.py
from typing import List

"""
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，
ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        """
        单调栈
        :param nums:
        :return:
        """
        # 维护一个单调递減栈
        ret = float('-inf')
        stack = []
        for num in reversed(nums):
            if ret > num:
                return True
            # 找到次大值
            while stack and stack[-1] < num:
                ret = stack.pop()
            stack.append(num)

        return False


if __name__ == '__main__':
    print(Solution().find132pattern([3, 1, 4, 2]))

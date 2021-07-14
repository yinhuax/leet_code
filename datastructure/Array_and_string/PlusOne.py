#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/11 15:17
# @File    : PlusOne.py
from typing import List

"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''

        tmp = 1
        for i in digits[::-1]:
            cur = i + tmp
            cur_num = cur % 10
            tmp = cur // 10

            result = str(cur_num) + result

        if tmp > 0:
            result = str(tmp) + result

        return [int(i) for i in result]


if __name__ == '__main__':
    print(Solution().plusOne(digits=[9, 9, 9]))

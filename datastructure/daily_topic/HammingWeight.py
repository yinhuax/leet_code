#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/22 7:47
# @File    : HammingWeight.py


class Solution:

    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret


if __name__ == '__main__':
    print(Solution().hammingWeight(11111111111111111111111111111101))

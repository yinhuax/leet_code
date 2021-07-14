#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 14:43
# @File    : FourSumCount.py
from typing import List

"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-lockup-table/xheops/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        四数相加二
        :param A:
        :param B:
        :param C:
        :param D:
        :return:
        """
        # 哈希表做法
        lookup = dict()
        for i in A:
            for j in B:
                sums = i + j
                lookup.setdefault(sums, 0)
                # 出现次数+1
                lookup[sums] += 1

        ans = 0
        for n in C:
            for m in D:
                if -(n + m) in lookup:
                    ans += lookup[-(n + m)]

        return ans

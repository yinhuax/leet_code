#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 15:33
# @File    : NumberOfBoomerangs.py
from typing import List

"""
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。
回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-lockup-table/xhp45m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        """
        哈希表
        :param points:
        :return:
        """
        ans = 0
        for i in points:
            cur_res = dict()
            for j in points:
                if i == j:
                    continue

                dist = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                cur_res[dist] = cur_res.get(dist, 0) + 1

            for k, v in cur_res.items():
                ans += v * (v - 1)

        return ans

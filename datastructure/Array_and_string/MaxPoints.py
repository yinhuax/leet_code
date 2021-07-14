#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 15:43
# @File    : MaxPoints.py
from typing import List

"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
"""


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        """
        哈希表做法，斜率相同的位于同一直线上
        :param points:
        :return:
        """
        res = 0
        if not points:
            return res

        for i in range(len(points)):
            ans = dict()
            same = 0
            cur_max = 0
            for j in range(i + 1, len(points)):
                # 计算斜率
                if points[j] == points[i]:
                    same += 1
                    continue
                if points[j][0] - points[i][0] == 0:
                    rate = float('inf')
                else:
                    rate = (points[j][1] - points[i][1]) * 1000 / (points[j][0] - points[i][0]) * 1000

                ans[rate] = ans.get(rate, 0) + 1
                cur_max = max(cur_max, ans[rate])

            res = max(res, cur_max + same + 1)

        return res


if __name__ == '__main__':
    print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))

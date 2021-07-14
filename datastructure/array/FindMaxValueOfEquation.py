#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/1 6:48
# @File    : FindMaxValueOfEquation.py
from typing import List

"""
给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。
也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。

请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。

题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-value-of-equation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        滑动窗口
        :param points:
        :param k:
        :return:
        """
        from collections import deque
        queue = deque([points[0]])
        ans = float("-inf")
        for p in points[1:]:
            # 滑动窗口新加元素导致窗口长度越界，则滑出左边元素直到符合边界条件
            while queue and p[0] - queue[0][0] > k:
                queue.popleft()
            if queue:
                ans = max(ans, p[1] + p[0] + queue[0][1] - queue[0][0])
            # 窗口从左到右保存的yi-xi是递减顺序;
            while queue and p[1] - p[0] > queue[-1][1] - queue[-1][0]:
                queue.pop()
            queue.append(p)
        return ans


if __name__ == '__main__':
    print(Solution().findMaxValueOfEquation(
        points=[[-19, -12], [-13, -18], [-12, 18], [-11, -8], [-8, 2], [-7, 12], [-5, 16], [-3, 9], [1, -7], [5, -4],
                [6, -20], [10, 4], [16, 4], [19, -9], [20, 19]], k=6))

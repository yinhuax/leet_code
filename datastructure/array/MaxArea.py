#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 6:50
# @File    : MaxArea.py
from typing import List

"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 
。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x96n4v/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class MaxArea(object):

    def __init__(self):
        pass

    def maxArea(self, height: List[int]) -> int:
        """
        双指针，对撞指针，额外空间O(1), 记录每次遍历的最大容器
        :param height:
        :return:
        """
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:

            if height[left] <= height[right]:
                max_area = max(max_area, height[left] * (right - left))
                # 低的空间内移
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1

        return max_area


if __name__ == '__main__':
    print(MaxArea().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/13 23:36
# @File    : FloodFill.py
from typing import List

"""
LC图像颜色渲染

有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/queue-stack/g02cj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class FloodFill(object):

    def __init__(self):
        pass

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        bfs 广度优先遍历方式
        :param image:
        :param sr:
        :param sc:
        :param newColor:
        :return:
        """
        from collections import deque
        init_color = image[sr][sc]
        if init_color == newColor:
            return image

        queue = deque()
        queue.append((sr, sc))

        row = len(image)
        col = len(image[0])

        while queue:
            for _ in range(len(queue)):
                cur_r, cur_c = queue.popleft()
                image[cur_r][cur_c] = newColor

                for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    tmp_x = cur_r + x
                    tmp_y = cur_c + y
                    if 0 <= tmp_x < row and 0 <= tmp_y < col and image[tmp_x][tmp_y] == init_color:
                        queue.append((tmp_x, tmp_y))

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        dfs 深度优先遍历方式
        :param image:
        :param sr:
        :param sc:
        :param newColor:
        :return:
        """
        init_color = image[sr][sc]
        # 如果初始颜色和新的颜色值相同，直接返回结果
        if init_color == newColor:
            return image

        row = len(image)
        col = len(image[0])

        def dfs(cur_x, cur_y):
            image[cur_x][cur_y] = newColor

            for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                tmp_x = cur_x + x
                tmp_y = cur_y + y
                if 0 <= tmp_x < row and 0 <= tmp_y < col and image[tmp_x][tmp_y] == init_color:
                    dfs(tmp_x, tmp_y)

        dfs(sr, sc)

        return image

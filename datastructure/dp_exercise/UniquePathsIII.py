#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 14:53
# @File    : UniquePathsIII.py
from typing import List

"""
在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        回溯算法
        :param grid:
        :return:
        """

        # 遍历一遍网格，记录起始位置，结束位置，需要经过0的次数
        n, m = len(grid), len(grid[0])
        start_i = 0
        start_j = 0
        todo = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                elif grid[i][j] == 0:
                    todo += 1

        self.ans = 0

        def dfs(i, j, todo):
            if todo == 0 and grid[i][j] == 2:
                self.ans += 1
                return

            tem = grid[i][j]
            grid[i][j] = -1
            for tmp_i, tmp_j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                index_i = tmp_i + i
                index_j = tmp_j + j
                if 0 <= index_i < n and 0 <= index_j < m and grid[index_i][index_j] != -1:
                    dfs(index_i, index_j, todo - 1)

            grid[i][j] = tem

        dfs(start_i, start_j, todo)
        return self.ans


if __name__ == '__main__':
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))

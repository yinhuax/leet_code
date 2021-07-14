#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/22 8:10
# @File    : PondSizes.py
from typing import List

"""
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度
。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pond-sizes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        """
        回溯算法
        :param land:
        :return:
        """
        n = len(land)
        m = len(land[0])

        def dfs(i, j):
            land[i][j] = 1

            self.count += 1
            for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, - 1)):
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < n and 0 <= tmp_j < m and not land[tmp_i][tmp_j]:
                    dfs(tmp_i, tmp_j)

        result = []

        self.count = 0
        for i in range(n):
            for j in range(m):
                if not land[i][j]:
                    self.count = 0
                    dfs(i, j)
                    result.append(self.count)

        result.sort()
        return result


if __name__ == '__main__':
    print(Solution().pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/17 15:11
# @File    : MatrixReshape.py
from typing import List

"""
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reshape-the-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        重塑矩阵
        :param nums:
        :param r:
        :param c:
        :return:
        """
        n = len(nums)
        m = len(nums[0])

        # 如果维度不相符，输出原矩阵
        if n * m != r * c:
            return nums

        result = []
        cur = []
        for i in range(n):
            for j in range(m):
                cur.append(nums[i][j])
                if (i * m + j + 1) % c == 0:
                    result.append(cur[::1])
                    cur.clear()

        return result


if __name__ == '__main__':
    print(Solution().matrixReshape(nums=
                                   [[1, 2],
                                    [3, 4]], r=1, c=4))

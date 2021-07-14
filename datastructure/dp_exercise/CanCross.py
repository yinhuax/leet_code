#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 21:47
# @File    : CanCross.py
from typing import List

"""
一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。

给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。
 开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

请注意：

石子的数量 ≥ 2 且 < 1100；
每一个石子的位置序号都是一个非负整数，且其 < 231；
第一个石子的位置永远是0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/frog-jump
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def canCross(self, stones: List[int]) -> bool:
        """
        动态规划

        dp[i][j] 表示上一步步数为j是否能达到i的位置
        :param stones:
        :return:
        """
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True

        for i in range(1, n):
            for j in range(i):
                diff = stones[i] - stones[j]

                if diff < 0 or diff >= n or not dp[j][diff]:
                    continue

                dp[i][diff] = True
                if diff - 1 >= 0:
                    dp[i][diff - 1] = True
                if diff + 1 < n:
                    dp[i][diff + 1] = True

        return any(dp[-1])

    def canCross1(self, stones: List[int]) -> bool:
        """
        dfs记忆化搜索
        :param stones:
        :return:
        """
        from functools import lru_cache
        end = stones[-1]
        s = set(stones)

        @lru_cache(None)
        def dfs(start, jump):
            if start == end:
                return True

            # 对应三种跳法
            for i in [jump + 1, jump, jump - 1]:
                if i <= 0:
                    continue
                if start + i in s and dfs(start + i, i):
                    return True

            return False

        return dfs(0, 0)


if __name__ == '__main__':
    print(Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17]))

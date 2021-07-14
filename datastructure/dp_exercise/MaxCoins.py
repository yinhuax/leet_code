#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 16:28
# @File    : MaxCoins.py
from typing import List

"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

 

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        动态规划：
        dp[i][j]  表示戳破i -> j 能获得的最大硬币
        :param nums:
        :return:
        """
        dp = [[0 for _ in range(len(nums) + 2)] for _ in range(len(nums) + 2)]
        nums = [1] + nums + [1]
        for i in range(len(nums) - 1, -1, -1):  # 枚举区间起点
            for j in range(i + 1, len(nums)):  # 枚举区间结尾
                for k in range(i + 1, j):  # 枚举区间各个点
                    dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j], dp[i][j])

        return dp[0][-1]

    def maxCoins1(self, nums: List[int]) -> int:
        """
        回溯算法
        :param nums:
        :return:
        """
        from functools import lru_cache

        @lru_cache(None)
        def helper(left, right):
            if left >= right - 1:
                return 0

            best = 0
            for i in range(left + 1, right):
                best = max(best, nums[left] * nums[i] * nums[right] + helper(i, right) + helper(left, i))

            return best

        nums = [1] + nums + [1]
        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    print(Solution().maxCoins1([3, 1, 5, 8]))

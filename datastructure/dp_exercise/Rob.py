#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 9:05
# @File    : Rob.py
from typing import List

"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def rob(self, nums: List[int]) -> int:
        """
        0表示不偷，1表示偷
        状态转移方程为dp[i][1] = dp[i - 1][0] + nums[i]
                    dp[i][0] = max(dp[i - 1][0], dp[i][1])
        :param nums:
        :return:
        """
        if not nums:
            return 0

        dp = [[0 for i in range(2)] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[-1])

    def rob1(self, nums: List[int]) -> int:
        """
        空间优化 o(n)
        状态转移方程为dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])，表示偷窃当前房间和不偷窃当前房间
        :param nums:
        :return:
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        """
        空间优化 o(1)
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)

        return max(first, second)


if __name__ == '__main__':
    print(Solution().rob2([1, 2, 3, 1]))

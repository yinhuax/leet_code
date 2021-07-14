#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 9:51
# @File    : Rob2.py
from typing import List

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def rob(self, nums: List[int]) -> int:
        """
        动态规则，转移方程为dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        需要注意这里如果偷了第一间房间，不能偷最后一间房间
        :param nums:
        :return:
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(self.dp(nums, 0, len(nums) - 1), self.dp(nums, 1, len(nums)))

    def dp(self, nums, start, end):
        dp = [0] * (end - start)
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start + 1])
        for i in range(start + 2, end):
            dp[i - start] = max(dp[i - 2 - start] + nums[i], dp[i - 1 - start])

        return dp[-1]


if __name__ == '__main__':
    print(Solution().rob(nums=[2, 3, 2]))

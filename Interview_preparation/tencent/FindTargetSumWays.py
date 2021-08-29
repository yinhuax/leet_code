#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/29 22:50
# @File    : FindTargetSumWays.py
from typing import List

"""
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        记忆化回溯
        :param nums:
        :param S:
        :return:
        """
        visited = dict()

        def dfs(i, sum_result, visited):
            if i < len(nums) and (i, sum_result) not in visited:
                visited[(i, sum_result)] = dfs(i + 1, sum_result - nums[i], visited) + \
                                           dfs(i + 1, sum_result + nums[i], visited)

            return visited.get((i, sum_result), sum_result == S)

        return dfs(0, 0, visited)

    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        """
        动态规划  dp[i][j]
        :param nums:
        :param S:
        :return:
        """
        sums = sum(nums)
        if sums < S or (sums + S) % 2:
            return 0

        target = (sums + S) // 2

        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        # 注意遍历范围
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                if j < num:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().findTargetSumWays(
        nums=[47, 30, 12, 40, 10, 31, 5, 12, 14, 25, 45, 34, 34, 31, 20, 1, 33, 28, 30, 30], S=34))

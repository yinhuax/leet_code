#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 10:17
# @File    : Jump2.py
from typing import List

"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def jump(self, nums: List[int]) -> int:
        """
        动态规划

        记录每个点之前的点能跳到当前位置最少次数
        dp[i] = min(dp[i - 1], dp[i - 2]..., dp[i - n]) + 1 条件是i - n + nums[i - n] >= i

        时间复杂度 O(N ** 2)
        :param nums:
        :return:
        """
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        cnt = 0
        for i in range(1, len(nums)):
            for j in range(cnt, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
                else:
                    cnt += 1

        return dp[-1]



if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))

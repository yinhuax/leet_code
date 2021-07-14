#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 22:16
# @File    : SplitArray.py
from typing import List

"""
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。

设计一个算法使得这 m 个子数组各自和的最大值最小。

 

示例 1：

输入：nums = [7,2,5,10,8], m = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:
        """
        二分查找, 左边界为数组最大值，右边界为数组和
        :param nums:
        :param m:
        :return:
        """

        def check(mid):
            sums = 0
            cnt = 1
            for num in nums:
                if sums + num > mid:
                    sums = num
                    cnt += 1
                else:
                    sums += num

            return cnt <= m

        left = 0
        right = 0
        for num in nums:
            left = max(left, num)
            right += num

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                # 满足条件
                right = mid
            else:
                left = mid + 1

        return left

    def splitArray1(self, nums: List[int], m: int) -> int:
        """
        动态规划

        dp[i][j]  表示数组的前i个数分割为j段所能得到的最大连续子数组和的最小值

        dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub(k + 1, i)))
        :param nums:
        :param m:
        :return:
        """
        # 构建前缀和
        sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if i == 0:
                sums[i + 1] = nums[i]
            else:
                sums[i + 1] = sums[i] + nums[i]

        dp = [[float('inf')] * (m + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 0

        for i in range(1, len(nums) + 1):  # 枚举每个子数组末尾
            for j in range(1, min(i, m) + 1):  # 枚举拆分的子数组个数
                for k in range(i + 1):  # 枚举每个拆分情况
                    dp[i][j] = min(dp[i][j], max(dp[k - 1][j - 1], sums[i] - sums[k - 1]))

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().splitArray1(nums=[7, 2, 5, 10, 8], m=2))

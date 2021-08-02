#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/30 17:29
# @File    : CheckSubarraySum.py
from typing import List

"""
给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        简单前缀和，超时，O(n ** 2)
        :param nums:
        :param k:
        :return:
        """
        sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            sums[i + 1] = nums[i] + sums[i]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) + 1):
                if (sums[j] - sums[i]) % k == 0:
                    return True

        return False

    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        """
        前缀和 + 同余定理
        (sums[j] - sums[i]) % k == 0  同理有 sums[i] % k == sums[i] % k
        :param nums:
        :param k:
        :return:
        """
        modes = set()
        presum = 0

        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k

            if presum in modes:
                return True

            modes.add(last)

        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum1([23, 2, 4, 6, 6], 7))

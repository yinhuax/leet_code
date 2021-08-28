#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/11 11:43
# @File    : GetSumAbsoluteDifferences.py
from typing import List

"""
给你一个 非递减 有序整数数组 nums 。

请你建立并返回一个整数数组 result，它跟 nums 长度相同，且result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和。

换句话说， result[i] 等于 sum(|nums[i]-nums[j]|) ，其中 0 <= j < nums.length 且 j != i （下标从 0 开始）。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-absolute-differences-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        前缀和
        :param nums:
        :return:
        """
        sums = [0] * (len(nums) + 1)
        n = len(nums)
        for i in range(1, len(sums)):
            sums[i] = sums[i - 1] + nums[i - 1]

        ans = []
        for i in range(1, len(sums)):
            # 当前位置结果 = (i * num[i - 1] - sums[i]) + (sums[-1] - sums[i] - nums[i - 1] * (n - i))
            res = (nums[i - 1] * i - sums[i]) + (sums[-1] - sums[i] - nums[i - 1] * (n - i))
            ans.append(res)

        return ans


if __name__ == '__main__':
    print(Solution().getSumAbsoluteDifferences([1, 4, 6, 8, 10]))

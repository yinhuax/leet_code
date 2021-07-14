#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/21 19:41
# @File    : LongestSubarray.py
from typing import List

"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        滑动窗口
        :param nums:
        :param limit:
        :return:
        """
        from collections import deque
        max_len = 1
        left = right = 0

        que_max, que_min = deque(), deque()
        while right < len(nums):
            while que_max and que_max[-1] < nums[right]:
                que_max.pop()

            while que_min and que_min[-1] > nums[right]:
                que_min.pop()

            que_min.append(nums[right])
            que_max.append(nums[right])

            while que_max and que_min and que_max[0] - que_min[0] > limit:
                if nums[left] == que_min[0]:
                    que_min.popleft()

                if nums[left] == que_max[0]:
                    que_max.popleft()

                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

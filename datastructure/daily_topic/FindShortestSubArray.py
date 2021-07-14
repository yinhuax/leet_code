#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/20 7:18
# @File    : FindShortestSubArray.py
from typing import List

"""
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

 

示例 1：

输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2：

输入：[1,2,2,3,1,4,2]
输出：6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        1. 计算最大频数，获取最大频数对应值
        2. 双指针遍历左右节点，找到第一个出现和最后一个出现位置
        :param nums:
        :return:
        """
        counter = dict()
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1

        result = sorted(counter.items(), key=lambda x: -x[1])
        max_len = result[0][1]
        ans = float('inf')
        for num, count in result:
            if count == max_len:
                left, right = 0, len(nums) - 1
                while nums[left] != num or nums[right] != num:
                    if nums[left] != num:
                        left += 1
                    if nums[right] != num:
                        right -= 1

                ans = min(ans, right - left + 1)
            else:
                break

        return ans

    def findShortestSubArray1(self, nums: List[int]) -> int:
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]

        max_num = min_len = 0
        for count, left, right in mp.values():
            if max_num < count:
                max_num = count
                min_len = right - left + 1
            elif max_num == count:
                min_len = min(min_len, right - left + 1)

        return min_len


if __name__ == '__main__':
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
